import urllib.request,time, sys, urllib.response
count = 1
while True:
	'''
	buka url freenet untuk dapatkan akses login
	'''
	try:
		request = urllib.request.Request("http://www.freenet.co.id/adIB/www/delivery/ck.php?n=a66315ae&cb=123")
		request.add_header("Cookie","OAID=1092ee97bc3beb1a7da076ca30bb23a8; OAVARS[a66315ae]=a%3A5%3A%7Bs%3A8%3A%22bannerid%22%3Bs%3A3%3A%22176%22%3Bs%3A6%3A%22zoneid%22%3Bs%3A3%3A%22167%22%3Bs%3A6%3A%22source%22%3Bs%3A3%3A%22IBS%22%3Bs%3A5%3A%22OXLCA%22%3Bi%3A1%3Bs%3A6%3A%22oadest%22%3Bs%3A56%3A%22http%3A%2F%2Fezxcess.antlabs.com%2Fwww%2Fpub%2Flogin%2Fsingleclick.php%22%3B%7D; OXLIA=176.nxvy2v-167; _OXBLC[176]=nxvy56; _OXLCA[176]=nxvy56-167");
		request.add_header("Referer","http://ads4.freenet.co.id/?site=1201")
		request.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0")
		request.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
		response = urllib.request.urlopen(request,None,100)
		print("Sukses, mencoba lagi..")
		count = count+1
		time.sleep(300)
	except:
		print("Error, mencoba lagi")