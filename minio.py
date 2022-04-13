mkdir -p  /jail/storage1 /jail/storage2 /jail/storage3 /jail/storage4
for I in {1..2}; do echo ${I}; tar --unlink -xpJf /jail/BASE/base.txz -C /jail/storage${I}; done
###########################################
for I in {3..4}
do
  cat >> /etc/jail.conf << __EOF
storage${I} {
  host.hostname = storage${I}.mwea.de;
  ip4.addr = 192.168.0.25${I};
  interface = re0;
  path = /jail/storage${I};
  exec.start = "/bin/sh /etc/rc";
  exec.stop = "/bin/sh /etc/rc.shutdown";
  exec.clean;
  mount.devfs;
  allow.raw_sockets;
}

__EOF
done
#############################################################
for I in {1..2}; do service jail onestart storage${I}; done
##############################################################

for I in {3..4}; do echo nameserver 1.1.1.1 > /jail/storage${I}/etc/resolv.conf; done
for I in {3..4}; do jexec storage${I} env ASSUME_ALWAYS_YES=yes pkg install -y minio; echo; done
for I in {1..2}; do jexec storage${I} which minio; done
###############################
for I in {1..2}
do
cat >> /jail/storage${I}/etc/hosts << __EOF
172.27.1.53 storage1.mwea.de
172.27.1.54 storage2.mwea.de
172.27.56.40 storage3.mwea.de
172.27.56.41 storage4.mwea.de
__EOF
done

################################

for DIR in {1..4}
do
  for I in {3..4}
  do
    jexec storage${I} mkdir -p /data${DIR}
  done
done
###############################
for I in {3..4}
  do
    echo storage${I}
    jexec storage${I} ls -1 / | grep data
    echo
  done
####################
    for DIR in {1..4}
    do
    for I in {1..4}
    do
        echo -n http://
        jls | grep storage${I}.mwea.de | awk '{printf $3}' | sed s/.local//g
        echo ":9000/data${DIR} \\"
    done
    done | sort -n



#########################################



 for DIR in {1..4}
do
  for I in {1..2}
  do
    echo -n https://
    jls | grep storage${I}.mwea.de| awk '{printf $3}' | sed s/mwea.de//g
    echo -n ":9000/data${DIR} "
  done
done | sort -n


for I in {3..4}
do
cat >> /jail/storage${I}/etc/rc.conf << __EOF
minio_enable=YES
minio_disks="http//storage1:9000/data1 http//storage2:9000/data1 http//storage1:9000/data2 http//storage2:9000/data2 http//storage1:9000/data3 http//storage2:9000/data3 http//storage1:9000/data4 http//storage2:9000/data4 http//storage3:9000/data1 http//storage4:9000/data1 http//storage3:9000/data2 http//storage4:9000/data2 http//storage3:9000/data3 http//storage4:9000/data3 http//storage3:9000/data4 http//storage4:9000/data4"
minio_console_address=":9001"
minio_env="MINIO_ACCESS_KEY='6gCA6hHRnBX72a MINIO_SECRET_KEY=zU3EZSb:u^`#z{kj"
minio_certs="/usr/local/etc/ssl"
__EOF
done



#######################

####
for DIR in {ad0..7}
do
  for I in {1..2}
  do
    jexec data${I} chmod u+rxw data${DIR}
  done
done
#######################

####
for I in {1..2}; do jexec storage${I} /usr/local/etc/rc.d/minio onestart ; echo; done

for I in {1..4}; do jexec storage${I} find /data?/test ; echo; done
for I in {ad0..4}; do zfs create 


find /data?/test




chown minio data${DIR}




&& chmod u+rxw data${DIR}






for DIR in 1 2 3 4
do
  for I in 3 4
  do
    echo -n http//
    jls | grep storage${I} | awk '{printf $3}' | sed s/.local//g
    echo -n ":9000/data${DIR} "
  done
done | sort -n


 for DIR in 1 2 3 4 
do
  for I in 3 4
  do
    echo -n http://
    jls | grep storage${I} | awk '{printf $3}' | sed s/.local//g
    echo ":9000/data${DIR} \\"
  done
done | sort -n


su -m minio -c 'env \\
MINIO_ACCESS_KEY=idkfa.qwe.123 \\
MINIO_SECRET_KEY=idkfa.qwe.123 \\
minio server \\
 --config-dir /usr/local/etc/minio \\
http://storage{1..4}.mwea.de:9000/{1...4} '


for DIR in {ad0..7}
do
  for I in {0..7}
  do
    zpool create -f data${I} ${DIR}
  done
done
