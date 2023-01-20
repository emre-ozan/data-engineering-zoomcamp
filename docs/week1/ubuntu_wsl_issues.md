## SSH issue 
I couldn't generate a ssh key for the github account because I couldn't access ~/.ssh folder. I solved this issue with the commands below.
```
sudo ssh-keygen -A
sudo /usr/sbin/service ssh start
```
### Connecting to GitHub with SSH
[Adding a new SSH key to your GitHub account](https://docs.github.- Generate a ssh key
```
ssh-keygen -t ed25519 -C "mremreozan@gmail.com"
```
- Copy the public ssh key into the github ssh settings 
```
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
```
- Test the github connection
```
ssh -T git@github.com
```

### Use SSH protocol for this repo
```
git remote set-url origin git@github.com:emre-ozan/data-engineering-zoomcamp.git
```
## Pip issue in the dockerfile
Add the nameserver line below into /etc/resolv.conf
- sudo nano /etc/resolv.conf
```
nameserver 8.8.8.8
```


