## ���з�ʽ

### һ������Python����

�ǵð�װ��```selenium```

```bash
pip install selenium
pip install tqdm
```

### �����������������

����ĿĬ����ChromeΪ������WindowsϵͳΪ�������������ԭ�����ơ���������ϵͳԭ�����ơ�

���ȵ�����Ҫ��װ��[Chrome�����](https://www.google.cn/chrome/index.html)����װ���ٵ�Chrome�ˣ�֮ǰ��ͬѧװ�˸���Chrome��������Ϊʲô��������������QAQ��

�����Ҫ����**��Ӧ�汾��**```ChromeDriver```��[���ص�ַ1](https://chromedriver.chromium.org/downloads)��[���ص�ַ2](https://googlechromelabs.github.io/chrome-for-testing/)��[���ص�ַ3](https://github.com/LetMeFly666/YuketangAutoPlayer/releases/download/v0.0/chromedriver.exe)��[�̳�1](https://blog.csdn.net/fighting_jiang/article/details/116298853)��[�̳�2](https://blog.csdn.net/zhoukeguai/article/details/113247342)��[���ĳ���](https://cn.bing.com/search?q=chromedriver%E4%B8%8B%E8%BD%BD)�����汾����Ļ�Ҳ����ν��

��```ChromeDriver.exe```�ŵ�```��������```�� �� ```�ű�(ִ��)Ŀ¼```�¡�

### ����������Ϣ

��```main.py```������ͷ������������Ϣ����Ҫ���Լ��޸ģ�

```python
IF_HEADLESS = False  # �Ƿ����޴���ģʽ���У��״����н���ʹ���д���ģʽ�Թ۲��Ƿ����Ԥ�ڣ�
COURSE_URL = 'https://grsbupt.yuketang.cn/pro/lms/84eubUXLHEy/17556639/studycontent'  # Ҫˢ�Ŀεĵ�ַ����ȡ��ʽ��README��
COOKIE = 'sjfeij2983uyfh84y7498uf98ys8f8u9'  # ����Ҳ��Ҫ���߱���Ŷ����ȡ��ʽ��README��
```

#### ��IF_HEADLESS

�Ƿ����޴���ģʽ���С��������д���ģʽ���У��ǾͲ��ø���һ���ˣ���

�����޴���ģʽ���У��򲻻ᵯ��Chrome��������棬����Ƶ��������ˢȡ��

#### ��COURSE_URL

��Ҫˢ�Ŀε�URL��

��������ã���������Ҫ��ȡ�𰸵Ŀγ̣������ѧϰ���ݡ������Ƶ�ַ����url���ɡ�

![how-to-get-url](img/how-to-get-url.jpg)

��ע����https��ʽ��Ŷ��

#### ��COOKIE

**�������COOKIE�Ļ�ȡ�Ƚ��鷳�������ѡ��[������һ��](#�Ŀ�ʼˢ��)��ÿ������ɨ���¼**��ɨ���¼��֧��HEADLESSģʽ��

COOKIE������������������㡣��ȡ��ʽ���£�

��¼������ѧУ�ģ�����ã�```�򿪿����߹���```����ͼ�Ĳ���1��Ҳ�ɰٶȣ������ε����Ӧ�á��洢��Cookie�� https&#58;&#47;&#47;xxx.yuketang... ��������**sessionid**��Ӧ��ֵ

![/how-to-get-cookie](img/how-to-get-cookie.jpg)

### �ġ��޸�Xpath
��ͬ�Ŀγ̵Ĵ�λ�ò�ͬ�밴���޸�
![/xpath](img/xpath.png)

### �塢�޸������ʽ
��ͬ�Ŀγ̵������ʽ��ͬ�밴���޸�

### �������г���
����`python main.py`������

## �ο���Ŀ
https://github.com/LetMeFly666/YuketangAutoPlayer