from obrtester.tester import tester
from obrtester.compare import comparison

if __name__ == '__main__':
    try:
        while True:
            print("1 For Datamatrix\n"
                  "2 For Image Comparison")
            prog =         input("What do you want to run? ")
            if prog == '1':
                version =  input('What version?            ')
                tester(version)
            elif prog == '2':
                type =     input('NGS or GS:               ')
                version =  input('First Version:           ')
                version2 = input('Second Version:          ')
                img_loc1 = input('First Image Folder:      ')
                img_loc2 = input('Second Image Folder:     ')
                comparison.compare_whole_folder(type, img_loc1, img_loc2, version, version2)
            else:
                break
            break
    except KeyboardInterrupt:
        pass
