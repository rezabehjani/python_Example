#https://github.com/wit-ai/pywit

from wit import Wit

client = Wit("BNV7QWMKHBG3NPILU6BVZ5EZR3DMRM5W")
# client.message('set an alarm tomorrow at 7am')

resp = None
with open('test.wav', 'rb') as f:
    resp = client.speech(f, None, {'Content-Type': 'audio/wav'})
print('Yay, got Wit.ai response: ' + str(resp))