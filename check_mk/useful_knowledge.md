- Location of check-mk-agent plugin:
`
/usr/lib/check_mk_agent/plugins
`

Place missing plugin in there in order to fix warn/error like this:
`
WARN - [agent] Version: 1.2.6p12, OS: linux, Missing agent sections: logwatch, execution time 0.4 sec
`
