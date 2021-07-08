from xml.dom import minidom as m

if __name__ == '__main__':
    job_list = []
    # 读取文件，得到每一行的job名称
    with open('job_list.txt') as jl:
        while True:
            line = jl.readline().strip()
            job_list.append(line)
            if not line: break

    job_list = job_list[:-1]
    print(job_list)
    # 遍历job_list
    for job in job_list:
        print('开始处理job:{}'.format(job))
        #  读取对应位置的xml
        xml_path_format_str = '/home/hudson/.jenkins/jobs/{}/config.xml'
        job_name = job
        xml_path_str = xml_path_format_str.format(job_name)

        dom = m.parse(xml_path_str)
        #获取publishers标签
        valeurs = dom.getElementsByTagName("publishers")
        # 读取要添加的xml
        dom_plugin = m.parse('plugin.xml')
        dom_ele_plugin = dom_plugin.getElementsByTagName(
            'org.jenkinsci.plugins.postbuildscript.PostBuildScript')[0]

        # 插入到publishers节点
        valeurs[0].appendChild(dom_ele_plugin)

        # 替换写config.xml
        try:
            with open(xml_path_str, 'w', encoding='UTF-8') as fh:
                # 4.writexml()第一个参数是目标文件对象，第二个参数是根节点的缩进格式，第三个参数是其他子节点的缩进格式，
                # 第四个参数制定了换行格式，第五个参数制定了xml内容的编码。
                dom.writexml(fh, indent='', addindent='\t', newl='',
                             encoding='UTF-8')
                print('OK')
                print('成功处理job:{}'.format(job))

        except Exception as err:
            print('处理job:{} 出错！！！'.format(job))
            print('错误：{err}'.format(err=err))
            continue
