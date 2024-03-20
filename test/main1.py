
def flatten_list(nested_lst):
    def flt_help(lst):

        flttn_list= []

        for elm in lst:
            if isinstance(elm,list):
               flttn_list.extend(flt_help(elm))
        
            else:
               flttn_list.append(elm)

        return flttn_list

    return flt_help(nested_lst)

nested_lst = [[1, 2, [3]], 4, [5, [6, 7]]] 
print (flatten_list(nested_lst))


