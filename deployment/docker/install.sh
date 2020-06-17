#!/bin/bash
which ssh-agent || ( apt-get update -y && apt-get install openssh-client -y )
eval $(ssh-agent -s)

#Make the ssh folder
mkdir -p ~/.ssh
chmod 700 ~/.ssh
echo "A"
echo $SSH_PRIVATE_KEY
echo $SSH_KNOWN_HOSTS
echo "B"
GITLAB_SERVER_NAME="gitlab.hydra.org.uk"
# GITLAB_SERVER_IP=$( dig +short $GITLAB_SERVER_NAME )
echo "Found '$GITLAB_SERVER_NAME': '$GITLAB_SERVER_IP'"
if [ -z "$GITLAB_SERVER_IP" ]
then
  echo "Impossible find the gitlab server '$GITLAB_SERVER_NAME'. Abort the build!"
  exit 1
fi
echo "$GITLAB_SERVER_IP  $GITLAB_SERVER_NAME" >> /etc/hosts

#Add the private key which has been passed in from the make file, via the docker file
echo $SSH_PRIVATE_KEY | tr '#' '\n' > ~/.ssh/key.pem
chmod 400 ~/.ssh/key.pem
ssh-add ~/.ssh/key.pem

#Add the known hosts environment variable to the known_hosts file. Ssh won't work automatically without this
echo "$SSH_KNOWN_HOSTS" > ~/.ssh/known_hosts
chmod 644 ~/.ssh/known_hosts

# Install all the dependencies
pipenv install --system --deploy --verbose

# Clean up the cache
rm -rf ~/.cache/pip

#Remove the ssh key so it doesn't get saved in the image
#rm ~/.ssh/key.pem
