<html>
<head>
    <title></title>
</head>
<body>
<pre>    <script type="text/javascript" >               
        var n = parseInt(prompt("enter the value n:"));
        var i = 1;
        main(i);
        function main(k) 
        { 
            if (k <= n) { 
                document.writeln(k);
                k++;
                main(k); 
            } 
            return 0; 
        } 
    </script>
</pre>
</body>
</html>