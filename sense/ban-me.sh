for i in $(seq 0 15);do
curl -i -s -k -X $'POST' \
    -H $'Host: 10.10.10.60' -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Referer: https://10.10.10.60/' -H $'Content-Type: application/x-www-form-urlencoded' -H $'Content-Length: 118' -H $'Origin: https://10.10.10.60' -H $'DNT: 1' -H $'Connection: close' -H $'Cookie: PHPSESSID=21eb656c9c5f0b7a7aa64f8e6d866175; cookie_test=1577971902' -H $'Upgrade-Insecure-Requests: 1' \
    -b $'PHPSESSID=21eb656c9c5f0b7a7aa64f8e6d866175; cookie_test=1577971902' \
    --data-binary $'__csrf_magic=sid%3A4be0653d1e5431ccd0400e7e602d5e258d10c530%2C1577968302&usernamefld=gyan&passwordfld=gyan&login=Login' \
    $'https://10.10.10.60/index.php'

echo $i
done
