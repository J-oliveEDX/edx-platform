echo "custom compile script test, jay"
sleep 2
sudo -H -u edxapp bash
source /edx/app/edxapp/edxapp_env
cd /edx/app/edxapp/edx-platform
paver update_assets lms --settings=production
exit
cd /edx/app/edxapp/edx-platform
echo "script finished"
