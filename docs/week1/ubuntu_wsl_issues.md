## SSH issue 
I couldn't generate a ssh key for the github account because I couldn't access ~/.ssh folder. I solved this issue with the commands below.
```
sudo ssh-keygen -A
sudo /usr/sbin/service ssh start
```
### Generate a ssh key
```
ssh-keygen -t ed25519 -C "mremreozan@gmail.com"
```
### Connecting to GitHub with SSH
[Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

### Use SSH protocol for this repo
```
git remote set-url origin git@github.com:emre-ozan/data-engineering-zoomcamp.git
```


