from flask import Flask, render_template, request
import WinEXP
import ScanAVname

app = Flask(__name__)


@app.route('/',  methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/WinExp',  methods=['POST'])
def Exps():
    systeminfo = request.form.get('systeminfo')
    exp, os = WinEXP.echo(systeminfo)
    echo = '此系统可能利用：'
    if not exp:
        echo = '未查询到可利用exp'
    else:
        for i in exp:
            echo += i + '、'
    html = '''
        <script>window.alert("{}");</script>
        <script>window.location.href="/"</script>
        '''.format(echo.strip('、'))
    return html


@app.route('/AVname',  methods=['POST'])
def AVname():
    tasklist = request.form.get('av')
    avname = ScanAVname.get_avname(tasklist)
    echo = '此系统可能有：'
    if type(avname) == list:
        for i in avname:
            echo += i+'、'
    elif type(avname) == str:
        echo = '未发现杀软进程'
    html = '''
    <script>window.alert("{}");</script>
    <script>window.location.href="/"</script>
    '''.format(echo.strip('、'))
    return html


if __name__ == '__main__':
    app.run()
