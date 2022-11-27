import time
import hmac
from requests import Request

print(time.time())
ts = int(time.time() * 1000)
print(ts)
request = Request('GET', '<api_endpoint>')
prepared = request.prepare()
signature_payload = f'{ts}{prepared.method}{prepared.path_url}'
if prepared.body:
    signature_payload += prepared.body
signature_payload = signature_payload.encode()
signature = hmac.new('YOUR_API_SECRET'.encode(), signature_payload, 'sha256').hexdigest()

request.headers['FTX-KEY'] = 'YOUR_API_KEY'
request.headers['FTX-SIGN'] = signature
request.headers['FTX-TS'] = str(ts)

# Only include this line if you want to access a subaccount. Remember to URI-encode the subaccount name if it contains special characters!
# request.headers['FTX-SUBACCOUNT'] = urllib.parse.quote('my_subaccount_name')