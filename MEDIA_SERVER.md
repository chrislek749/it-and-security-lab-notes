# Self-built PC to home media server

Confirmed: you assembled the whole PC, including CPU, GPU, RAM and PSU. This is a completed hardware project. The media-server conversion has not been performed. OS, component models, RAM capacity, free storage and setup date are still needed.

## What you are making
A media server stores and organises videos, music or photos on the PC and lets a phone, TV or another computer play them over your home network. Proposed software: Jellyfin. This is configuration and testing, with no programming required. Use your own recordings or media you have permission to use.

## Plan after we confirm the PC details
1. Record OS, CPU/GPU, RAM, free disk space and the device you want to play media on
2. Back up important existing data; retain the current OS unless a change is explicitly agreed
3. Install the appropriate Jellyfin server package from its official site and follow its initial setup wizard
4. Add a small folder containing two or three harmless test media files and check their library entries
5. Create a normal viewer account separate from the administrator and give it access only to the test library
6. Test playback on the PC, then an authorised device on the same trusted home network
7. Check whether playback is direct or requires transcoding before configuring any GPU acceleration; capability depends on exact hardware, codecs and OS
8. Test what happens when the PC sleeps or the server stops. Write down the limitation rather than claiming 24/7 availability
9. Document how to stop the service, remove its firewall exception if added and restore the prior setup

Keep this first project local to the home network. No router forwarding, public server or disabled firewall is needed. The specific installer and any firewall rule depend on the confirmed OS. Password entry stays with you.

## Test record to complete
| Test | Expected | Actual |
|---|---|---|
| Local playback | Test file plays | Not run |
| Second-device playback | Authorised viewer can play | Not run |
| Restricted library | Viewer cannot access excluded content | Not run |
| Server stopped | Playback becomes unavailable; recovery documented | Not run |

Save redacted screenshots of the library and user permissions, exact hardware/software details and your completed test table. Avoid including credentials, private media or public IP addresses in the portfolio.

Current CV wording: Assembled a personal desktop computer, installing the CPU, GPU, RAM and power supply

After server setup and testing: Repurposed a self-built PC as a Jellyfin media server, configured a separate viewer account and verified playback across two home devices

The second bullet is conditional on completing those exact tasks. This plan was prepared by AI; you should explain your own setup choices and troubleshooting.

The previous file-server README is an optional alternative, not the selected project.

Official starting point: https://jellyfin.org/docs/general/quick-start/
