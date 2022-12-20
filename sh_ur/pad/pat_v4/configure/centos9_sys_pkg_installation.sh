# Download and enable repo
# For centos 9.

wget https://forensics.cert.org/cert-forensics-tools-release-el9.rpm
rpm -Uvh cert-forensics-tools-release*rpm
yum --enablerepo=forensics install antiword



