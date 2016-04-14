<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="zh-cn">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<title>php</title>
<link rel="stylesheet" href="style.css" type="text/css">
<script type="text/javascript" src="/js/jquery.js"></script>
<script type="text/javascript" src="index.js"></script>
<script type="text/javascript" src="/js/mousetrap.min.js"></script>
<style type="text/css">
	*:focus{ outline: none; }
	iframe, form, body,html{height: 100%;}
	#top{padding:10px;}
	#left{width:50%;float:left; height: 100%;}
	#right{width:50%;float:right; height: 100%;}
	iframe{display: block; width: 95%; margin:10px 10px 0 0; border: 1px solid #ccc;}
</style>
<script type="text/javascript">
$(function() {
	$("#code").linedtextarea(
		{selectedLine: 61}
	);
 Mousetrap.bind('ctrl+enter', function(e){
     $('form').submit()
 })

 });

</script>
</head>
<body>
	<div id="top"></div>
	<div id="left">
		<form action="/cgi-bin/php.py" method="post" target="result">
			<input type="submit" value="执行"><br>
			<textarea id="code" class="mousetrap" name="code" style="width:95%;height:100%;">&lt;!doctype html&gt;
&lt;html lang="zh"&gt;
&lt;head&gt;
&lt;meta charset="UTF-8"&gt;
&lt;title&gt;Document&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;?php
    
?&gt;
&lt;/body&gt;
&lt;/html&gt;
</textarea>
		</form>
	</div>
	<div id="right">
		<iframe name="result"></iframe>
	</div>
</body>
</html>
