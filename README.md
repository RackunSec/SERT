# SERT
## Spirion EnCase Reporting Tool

This tool will check the current evidence file, mounted as an E01 EnCase file, and match the Spirion results for generating reports for litigation purposes.

## Mount EWF (E01) Image in Debian
To mount the Expert Witness File, you first need to install a few items from the Debian APT repository.
```
root@demon:~# apt install ewf-tools -y
```
Next, we need to mount the raw image to create a file descriptor that we can then mount using the proper file system of the original drive that was copied to the image.
```
root@demon:~# mkdir /mnt/raw
root@demon:~# ewfmount /path/to/file.e01 /mnt/raw
```
Now, we can mount the file descriptor image ```/mnt/raw/ewf1```, but first we need the byte offset to the partition we want to analyze.
```
root@demon:~# fdisk -l /mnt/raw/ewf1
Device              Start        End   Sectors   Size Type
/mnt/raw/ewf1p1      2048     206847    204800   100M EFI System
/mnt/raw/ewf1p2    206848     468991    262144   128M Microsoft reserved
/mnt/raw/ewf1p3    468992  998543625 998074634 475.9G Microsoft basic data
/mnt/raw/ewf1p4 998545408 1000212479   1667072   814M Windows recovery environment
```
In my case above, it is ```/mnt/raw/ewf1p3```. That offset is ```468992``` as shown above. So, we multiply that by 512 (which can do using Bash and interpolation during the mount command) like so,
```
root@demon:~# mkidr /mnt/evidence
mount /mnt/raw/ewf1 /mnt/evidence/ -o ro,loop,show_sys_files,streams_interace=windows,offset=$((468992*512))
```
We can now run SERT tool with this as the evidence PATH.

## Referfences

[Mounting EWF Images with Linux](https://www.andreafortuna.org/2018/04/11/how-to-mount-an-ewf-image-file-e01-on-linux/)

[Spirion](https://www.spirion.com/)

[EnCase](https://www.guidancesoftware.com/encase-forensic)
