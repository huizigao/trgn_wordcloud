import os

# define input / output
in_path_txt = '/home/huizigao/assignments/trgn_wordcloud/my_webpages.txt'
out_path = '/home/huizigao/assignments/trgn_wordcloud/current_pages'
out_path_txt = os.path.join(out_path, 'my_current.txt')
out_png_path = os.path.join(out_path, 'wordcloud.png')

# prepare folders
os.makedirs(out_path, exist_ok=True)
os.system('cd {}'.format(out_path))

# read files
with open(in_path_txt) as f:
    # iteratively parsing inputs
    for index, link in enumerate(f):
        out_file_path = os.path.join(out_path, 'file{}.html'.format(index+1))

        # perform downloading
        os.system('wget {} -O {}'.format(link.strip('\n'), out_file_path))

        # save out my_current.txt
        if index <= 0:
            os.system('html2text.py {} > {}'.format(out_file_path, out_path_txt))
        else:
            os.system('html2text.py {} >> {}'.format(out_file_path, out_path_txt))

    # mark line numbers
    os.system('wc -l {} >> {}'.format(out_path_txt, out_path_txt))

    # generate wordcloud
    os.system('wordcloud_cli --text {} --imagefile {}'.format(out_path_txt, out_png_path))