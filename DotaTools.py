#  DotaTools main tool
#  Written by MarcusMunch
#  http://marcusmunch.github.com

import settings
import os

def upload(toUpload=False):
    if not settings.FTP_ADDR:
        print "No FTP settings were found. Skipping upload..."
    if toUpload and settings.FTP_ADDR:
        try:
            print ('Uploading %s...' % toUpload)
            ftp = FTP(settings.FTP_ADDR)
            ftp.login(settings.FTP_ADDR, settings.FTP_PASS)
            if not 'DotaTools' in ftp.nlst():
                print 'Folder "DotaTools" not found. Creating...'
                ftp.mkd('DotaTools')
            ftp.cwd('DotaTools')
            file = open('output/' + toUpload, 'r')
            if settings.DEBUG_MODE is False:
                ftp.storbinary('STOR ' + outFile, file)
            file.close()
            print 'Uploaded file to FTP at ' + settings.FTP_ADDR + '. Closing connection...\n'
            ftp.quit()
        except:
            print ('Unexpected error!'), sys.exc_info()

def writeToFile(output="", outFile=""):
    if outFile == "":
        print "No output selected - no file written"
    else:
        if not os.path.exists('output'):
            print 'Folder "output" not found. Creating...\n'
            if settings.DEBUG_MODE is False: os.mkdir('output')
        print ('Writing to file %s: "%s"' % (outFile, output))
        if settings.DEBUG_MODE is False:
            file = open('./output/' + outFile, "w")
            file.write(output)
            file.close
        print "Successfully wrote to file!\n"

if __name__ == '__main__':
	print "Whoops! This script isn't meant to be run this way - it merely contains some of the functions used by the actual scripts within this folder!"