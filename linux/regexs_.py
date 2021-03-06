ip_regex = r"\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}"
Time_regex = r"\d{1,2}\/\D+\d{4}\:\d{1,2}:\d{1,2}[:]\d{1,2} [+|-]\d+"
Method_regex = r"(GET|POST)+"
Path_regex = r"\/\D+\/\D+[.]\D+"
Status_regex = r"\d+"
DataSize_regex = r"\d+"
Suspicious_Extension_regex = r"(.php|.phtml|.inc|.jsp|.jsf|.asp|.asa|.cds|.cer|.aspx|.asax|.ascx|.ashx|.asmx|.axd|.config|.cs|.csproj|.licx|.licx|.rem|.resources|.resx|.soap|.vb|.vbproj|.vsdisco|.webinfo)"
Sql_injection_regx = r"/((\%3D)|(=))[^\n]*((\%27)|(\')|(\-\-)|(\%3B)|(;))/i"
CssAttack_regx = r"/((\%3C)|<)((\%2F)|\/)*[a-z0-9\%]+((\%3E)|>)/ix"
Str_dot = "[.]"


#https://www.symantec.com/connect/articles/detection-sql-injection-and-cross-site-scripting-attacks
