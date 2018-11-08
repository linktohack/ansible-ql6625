#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'domain': self.domain,
            'letsencrypt': self.letsencrypt
        }
 
    def domain(self, domain, env):
        return domain + ('' if env == 'production' else '.staging') + '.ql6625.fr'

    def letsencrypt(self, sites, env, domain):
        domains = [ ' -d ' + it['domain'] + ('' if env == 'production' else '.staging') + '.ql6625.fr' for it in sites ]
        return 'certbot --agree-tos --staging certonly --expand --webroot -w /var/lib/letsencrypt -m dev@ql6625.fr -d ' + domain + ''.join(domains)
