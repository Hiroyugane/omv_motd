#!/usr/bin/env python3
# Status: copied over existing code that will be reworked here.
#         Hasn't been edited yet
# Debug Info
from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())
#


#mandriva-based nginx-docker used. Completely left out for now since standard system wont have webservers
r''' (raw-string for preventing pylint-warnings)
#find certificates and their status
def certificate_status():
    # cert file to use, maybe put fallback-search in but put main input in config file
    cert_file = '/var/lib/openmandriva/omv/docker-nginx/abf.openmandriva.org-chain.pem'
    if(os.path.isfile(cert_file)):
        # scrape certificate text (whatever that means?)
        certificate_text = run_cmd('openssl x509 -noout -in ' + cert_file +' -text')
        # search some match for the renew-date?
        category_match = re.search('\W*Not After[^:]*:(.+)', certificate_text)
        # scrape due-date from match
        due_date = category_match.group(1)
        # return when cert is going to expire
        certificate = {'cert_expiration': '[%s]' % (str(due_date))}
        return(certificate)
'''