#!/bin/bash

cat /dev/null > productlist.csv
echo productcode,productname,price >> productlist.csv

productcode=

for (( i=1; i<10000; i++))
do
	if [ $i -lt 10 ]
	then
		productcode=C0000$i
	elif [ $i -lt 100 ]
	then
		productcode=C000$i
	elif [ $i -lt 1000 ]
	then
		productcode=C00$i
	elif [ $i -le 9999 ]
	then
		productcode=C0$i
	fi

	python atomy_member_price.py $productcode > $productcode.html

	productname=$(grep tGdsName $productcode.html | sed -e 's/<[^>]*>//g' | tr -d '\r')
	price=

	if [ ! -z "$productname" ]
	then
		price=$(grep "red numberic price" $productcode.html | grep -E -o '\<[0-9]{1,4}\.[0-9]{2}\>')
		echo $productcode,${productname##*( )},$price >> productlist.csv
	fi
	rm $productcode.html
done
