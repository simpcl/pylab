
import tfs

if __name__ == '__main__':
    name = tfs.encode_fsname(1, 8)
    print name
    appid, fileid = tfs.decode_fsname(name)
    print "appid: ", appid
    print "fileid:", fileid
