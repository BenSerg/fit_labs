pages, strings_count, symbols_count, bytes_in_symbol = 100, 50, 25, 4
disk_size_mb = 1.44
disk_bytes = disk_size_mb * 1024 ** 2
print("Количество книг, помещающихся на дискету:",
      int(disk_bytes // (bytes_in_symbol * symbols_count * strings_count * pages)))
