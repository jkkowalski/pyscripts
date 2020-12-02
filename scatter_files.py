from os import link, listdir, path, mkdir
import sys
 
work_dir = sys.argv[1]
number_of_buckets = int(sys.argv[2])

bucket_template

out_dirs = list(list((0, path.join(cwd, '%02d' % x ))) for x in range(number_of_buckets))
out_dirs.sort()
 
for d in out_dirs:
  mkdir(d[1])
 
in_files = listdir(cwd)
 
for f in in_files:
    s = path.getsize(path.join(cwd, f))
    link(path.join(cwd, f), path.join(out_dirs[0][1], f))
    out_dirs[0][0] += s
    out_dirs.sort()
 
 
    for d in out_dirs:
      link(path.join(cwd, f), path.join(d[1], f)) 
