import datetime
import os
import sys

git_repository=['repo-name1','repo-name2']
current_date=os.system('date +%d-%m-%Y')
now = datetime.datetime.now()
directory="codecommit_backup_" + now.strftime('%d-%m-%Y')
if not os.path.exists(directory):
    print "creating directory for codecommit"
    os.makedirs(directory)
    os.chdir(directory)
else:
    print "Repo already"
    exit(-1)


##Function to fetch repo and send to S3 bucket
def code_commit_repo():

  for repo in git_repository:
      cloneCmd = "git clone --bare ssh://git-codecommit.eu-west-1.amazonaws.com/v1/repos/" + repo + " .git"
      print(cloneCmd)
      print(repo)

      os.makedirs(repo)
      os.chdir(repo)
      os.system(cloneCmd)
      os.chdir("..")

def s3_bucket():
    os.chdir("..")
    zipFile = "zip" + " " + directory + ".zip" + " " "-r" + " " + directory
    s3Bucket = "s3_bucket_name"
    s3File = "aws s3 cp" + " " + directory + ".zip" + " " " s3://" + s3Bucket
    os.system(zipFile)
    os.system(s3File)
    os.system("rm -rf" + " " + directory + "*")
    print s3File

code_commit_repo()
s3_bucket()
