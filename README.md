# cvem-toolkit

Manages Cisco Video Codecs including DX, SX, and MX series devices


Endpoint Deployment:
-Requires csv file of all configs you wish to have applied.
  -Pull backup config of existing device
  -Change config to contain static info which is true for your environment
  -Remove the following lines (as they "usually" change dynamically per endpoint):
    xConfiguration H323 Profile 1 H323Alias E164:
    xConfiguration H323 Profile 1 H323Alias ID:
    xConfiguration SIP DisplayName:
    xConfiguration SIP URI:
    xConfiguration SystemUnit Name:
  -Name csv tpeconfig.csv and save it in the "Resources" directory
