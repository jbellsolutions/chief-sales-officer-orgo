"""Create CSO routines once in the installed Hermes scheduler. Explicit --enable required."""
import argparse,json,os
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]

def install(channel, enable=False):
    if not channel.startswith(('C','D','G')) or not channel.isalnum():
        raise ValueError('Slack conversation ID required')
    hermes=next((p for p in [Path('/usr/local/lib/hermes-agent'),Path.home()/'.hermes/hermes-agent'] if (p/'cron/jobs.py').exists()),None)
    if not hermes:raise RuntimeError('Installed Hermes scheduler not found')
    sys.path.insert(0,str(hermes))
    from cron.jobs import create_job,list_jobs
    home=Path(os.environ.get('HERMES_HOME',str(Path.home()/'.hermes')))
    script=home/'scripts/cso-review.py';script.parent.mkdir(parents=True,exist_ok=True)
    script.write_text("import importlib.util,json\nfrom pathlib import Path\ns=importlib.util.spec_from_file_location('ledger','/opt/chief-sales-officer/cso/ledger.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)\nl=m.Ledger(Path.home()/'.hermes/cso/pipeline.db')\nr=l.review();r.pop('as_of',None);print(json.dumps(r,sort_keys=True));l.db.close()\n")
    script.chmod(0o700)
    existing={j.get('name'):j for j in list_jobs(include_disabled=True)}
    jobs=[]
    for name,cron in [('morning','0 9 * * 1-5'),('midday','0 13 * * 1-5'),('evening','0 17 * * 1-5'),('weekly','0 10 * * 5')]:
        title='CSO '+name
        if title in existing:
            job=existing[title]
            if job.get('deliver')!='slack:'+channel:raise ValueError('Existing CSO job uses another Slack destination; review before changing')
            jobs.append({'id':job['id'],'name':title,'status':'existing'});continue
        prompt=(ROOT/('routines/'+name+'.prompt')).read_text()+ '\nThe attached journal is local. Explicitly report unverified integrations. No sends, CRM mutations, paid actions or changes to other schedules. Use the provided snapshot and draft exact next steps for the owner.'
        kwargs={'monitor_script':str(script)} if name=='midday' else {'script':str(script)}
        job=create_job(prompt=prompt,schedule=cron,name=title,deliver='slack:'+channel,skills=['chief-sales-officer'],enabled_toolsets=['file'],workdir=str(ROOT),paused=not enable,paused_reason=None if enable else 'Awaiting owner activation',**kwargs)
        jobs.append({'id':job['id'],'name':title,'status':'enabled' if enable else 'paused','schedule':cron})
    print(json.dumps(jobs,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--channel',required=True);p.add_argument('--enable',action='store_true');a=p.parse_args();install(a.channel,a.enable)
