import re
from urllib.parse import urlparse

def extract_feature(url):
    parsed = urlparse(url)

    domain = parsed.netloc
    path = parsed.path

    url_length = len(url)
    domain_length = len(domain)
    has_ip = True if re.match(r'\d+\.\d+\.\d+\.\d+', domain) else False

    dot_count = url.count('.')
    hyphen_count = domain.count('-')
    has_at = True if '@' in url else False
    has_double_slash = True if '//' in url[8:] else False

    parts = domain.split('.')
    subdomain_count = len(parts)-1

    uses_https = True if parsed.scheme == "https" else False
    
    sus_keyword = ['login', 'verify', 'update', 'secure', 'bank',
                           'account', 'confirm', 'password', 'signin', 'free']
    
    lower_url = url.lower()
    #count = sum(1 for word in suspicious_keyword if word in lower_url)
    sus_keyword_count = 0
    for word in sus_keyword:
        if word in lower_url:
            sus_keyword_count += 1

    sus_tld = ['.xyz','.tk','.ml','.ga','.top']
    sus_tld_count = 0
    for tld in sus_tld:
        if tld in lower_url:
            sus_tld_count += 1
    return {
        'url_length':       url_length,
        'domain_length':    domain_length,
        'dot_count':        dot_count,
        'hyphen_count':     hyphen_count,
        'subdomain_count':  subdomain_count,
        'sus_keyword_count':sus_keyword_count,
        'sus_tld_count':    sus_tld_count,
        'has_ip':           has_ip,
        'has_at':           has_at,
        'has_double_slash': has_double_slash,
        'uses_https':       uses_https,
    }

if __name__ == "__main__":
    test_urls = [
        "https://www.google.com/search?q=python",               # Legit
        "http://paypal-secure-login.verify-account.xyz/update", # Phishing
        "http://192.168.1.1/bank/login?user=john&password=abc", # Phishing (IP)
    ]

    for url in test_urls:
        print((f"\nURL: {url}"))
        features = extract_feature(url)
        for feature, value in features.items():
            print(f" {feature:<20} = {value}")