manage="${VENV}/bin/python ${INSTALLDIR}/${REPO}/manage.py"

$manage migrate --noinput --settings=project.settings
chown -R ubuntu:ubuntu /var/praekelt/mobius-demo
su - ubuntu -c "source /home/ubuntu/.nvm/nvm.sh && cd /var/praekelt/mobius-demo &&  nvm install && npm install && npm run build"
$manage collectstatic --noinput --settings=project.settings
