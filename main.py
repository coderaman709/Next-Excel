from tkinter import *
from tkinter import filedialog
root = Tk()
root.geometry("1080x1920")
root.title("Next Excel -- By Aman")


def load():
       file = filedialog.askopenfilename()
       print(file)
       if file:
              fh = open(file, 'r')
              read = fh.read()
              ac_fm = list(str(read))
              print(ac_fm)
              vlue1 = ', '.join(ac_fm[0])
              vlue2 = ', '.join(ac_fm[1])
              a = ', '.join(ac_fm[4])
              fn_vlue = vlue1+vlue2
              print(fn_vlue)
              print(a)
              f_nm = file

              ttl_nm = Label(ttl_bar, text=f_nm, fg="white", font="bahnschrift 10", background="#24546a")
              ttl_nm.place(x=300, y=2)

              if(fn_vlue=="a1"):
                     pass
              

              # a1.insert(INSERT, read)
              # fh.close()
       else:
              print("ERRRRROR")


f_nm = "Untitled"


def saveFile():
       file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Text File", ".txt"), ("Html File", ".html"), ("Excel File", ".xlxs")])
       
       file = f_nm
       ttl_nm = Label(ttl_bar, text=f_nm, fg="white", font="bahnschrift 10", background="#24546a")
       ttl_nm.place(x=CENTER, y=2)


       prompt.place_forget()
       msg.place_forget()
       ok.place_forget()
       no.place_forget()
       can.place_forget()

       t1 = str(a1.get())
       file.write("a1: "+ t1 + " \n")

       t2 = str(a2.get())
       file.write("a2: "+ t2 + " \n")

       t3 = str(a3.get())
       file.write("a3: "+ t3 + " \n")

       t4 = str(a4.get())
       file.write("a4: "+ t4 + " \n")

       t5 = str(a5.get())
       file.write("a5: "+ t5 + " \n")

       t6 = str(a6.get())
       file.write("a6: "+ t6 + " \n")

       t7 = str(a7.get())
       file.write("a7: "+ t7 + " \n")

       t8 = str(a8.get())
       file.write("a8: "+ t8 + " \n")

       t9 = str(a9.get())
       file.write("a9: "+ t9 + " \n")

       t10 = str(a10.get())
       file.write("a10: "+ t10 + " \n")

       t11 = str(a11.get())
       file.write("a11: "+ t11 + " \n")

       t12 = str(a12.get())
       file.write("a12: "+ t12 + " \n")

       t13 = str(a13.get())
       file.write("a13: "+ t13 + " \n")

       s1 = str(b1.get())
       file.write("b1: "+ s1 + " \n")

       s2 = str(b2.get())
       file.write("b2: "+ s2 + " \n")

       s3 = str(b3.get())
       file.write("b3: "+ s3 + " \n")

       s4 = str(b4.get())
       file.write("b4: "+ s4 + " \n")

       s5 = str(b5.get())
       file.write("b5: "+ s5 + " \n")

       s6 = str(b6.get())
       file.write("b6: "+ s6 + " \n")

       s7 = str(b7.get())
       file.write("b7: "+ s7 + " \n")

       s8 = str(b8.get())
       file.write("b8: "+ s8 + " \n")

       s9 = str(b9.get())
       file.write("b9: "+ s9 + " \n")

       s10 = str(b10.get())
       file.write("b10: "+ s10 + " \n")

       s11 = str(b11.get())
       file.write("b11: "+ s11 + " \n")

       s12 = str(b12.get())
       file.write("b12: "+ s12 + " \n")

       s13 = str(b13.get())
       file.write("b13: "+ s13 + " \n")

       p1 = str(c1.get())
       file.write("c1: "+ p1 + " \n")

       p2 = str(c2.get())
       file.write("c2: "+ p2 + " \n")

       p3 = str(c3.get())
       file.write("c3: "+ p3 + " \n")

       p4 = str(c4.get())
       file.write("c4: "+ p4 + " \n")

       p5 = str(c5.get())
       file.write("c5: "+ p5 + " \n")

       p6 = str(c6.get())
       file.write("c6: "+ p6 + " \n")

       p7 = str(c7.get())
       file.write("c7: "+ p7 + " \n")

       p8 = str(c8.get())
       file.write("c8: "+ p8 + " \n")

       p9 = str(c9.get())
       file.write("c9: "+ p9 + " \n")

       p10 = str(c10.get())
       file.write("c10: "+ p10 + " \n")

       p11 = str(c11.get())
       file.write("c11: "+ p11 + " \n")

       p12 = str(c12.get())
       file.write("c12: "+ p12 + " \n")

       p13 = str(c13.get())
       file.write("c13: "+ p13 + " \n")

       file.close()
                 


def fuctns():
            ac_fm = list(str(fr_mla.get()))
            cor = ', '.join(ac_fm[0])
            vlue1 = ', '.join(ac_fm[1])
            vlue2 = ', '.join(ac_fm[2])
            vluem = ', '.join(ac_fm[3])
            vlue3 = ', '.join(ac_fm[4])
            try:
              vlue4 = ', '.join(ac_fm[5])
            except:
                   vlue4 = ', '.join(ac_fm[4])
            fn_vlue1 = vlue1+vlue2
            fn_vlue2 = vlue3+vlue4
            fn_vluem = vluem
            print(fn_vlue1)
            print(fn_vluem)
            print(fn_vlue2)
            if(cor!="="):
                   print("Error In Formula, a foumula must be start from the sign \'=\'")
                   prm.place(x=340, y=250)
                   msg2.place(x=370, y=270)
                   ok2.place(x=560, y=330)



            if(fn_vlue1=="a1"):
              val = a1.get()
            elif(fn_vlue1=="a2"):
                   val = a2.get()
            elif(fn_vlue1=="a3"):
                   val = a3.get()
            elif(fn_vlue1=="a4"):
                   val = a4.get()
            elif(fn_vlue1=="a5"):
                   val = a5.get()
            elif(fn_vlue1=="a6"):
                   val = a6.get()
            elif(fn_vlue1=="a7"):
                   val = a7.get()
            elif(fn_vlue1=="a8"):
                   val = a8.get()
            elif(fn_vlue1=="a9"):
                   val = a9.get()
            elif(fn_vlue1=="a10"):
                   val = a10.get()
            elif(fn_vlue1=="a11"):
                   val = a11.get()
            elif(fn_vlue1=="a12"):
                   val = a12.get()
            elif(fn_vlue1=="a13"):
                   val = a13.get()
            elif(fn_vlue1=="b1"):
                   val = b1.get()
            elif(fn_vlue1=="b2"):
                   val = b2.get()
            elif(fn_vlue1=="b3"):
                   val = b3.get()
            elif(fn_vlue1=="b4"):
                   val = b4.get()
            elif(fn_vlue1=="b5"):
                   val = b5.get()
            elif(fn_vlue1=="b6"):
                   val = b6.get()
            elif(fn_vlue1=="b7"):
                   val = b7.get()
            elif(fn_vlue1=="b8"):
                   val = b8.get()
            elif(fn_vlue1=="b9"):
                   val = b9.get()
            elif(fn_vlue1=="b10"):
                   val = b10.get()
            elif(fn_vlue1=="b11"):
                   val = b11.get()
            elif(fn_vlue1=="b12"):
                   val = b12.get()
            elif(fn_vlue1=="b13"):
                   val = b13.get()
            elif(fn_vlue1=="c1"):
                   val = c1.get()
            elif(fn_vlue1=="c2"):
                   val = c2.get()
            elif(fn_vlue1=="c3"):
                   val = c3.get()
            elif(fn_vlue1=="c4"):
                   val = c4.get()
            elif(fn_vlue1=="c5"):
                   val = c5.get()
            elif(fn_vlue1=="c6"):
                   val = c6.get()
            elif(fn_vlue1=="c7"):
                   val = c7.get()
            elif(fn_vlue1=="c8"):
                   val = c8.get()
            elif(fn_vlue1=="c9"):
                   val = c9.get()
            elif(fn_vlue1=="c10"):
                   val = c10.get()
            elif(fn_vlue1=="c11"):
                   val = c11.get()
            elif(fn_vlue1=="c12"):
                   val = c12.get()
            elif(fn_vlue1=="c13"):
                   val = c13.get()
            else:
                   pass
            
            # value 2
            if(fn_vlue2=="a1"):
                   val2 = a1.get()
            elif(fn_vlue2=="a2"):
                   val2 = a2.get()
            elif(fn_vlue2=="a3"):
                   val2 = a3.get()
            elif(fn_vlue2=="a4"):
                   val2 = a4.get()
            elif(fn_vlue2=="a5"):
                   val2 = a5.get()
            elif(fn_vlue2=="a6"):
                   val2 = a6.get()
            elif(fn_vlue2=="a7"):
                   val2 = a7.get()
            elif(fn_vlue2=="a8"):
                   val2 = a8.get()
            elif(fn_vlue2=="a9"):
                   val2 = a9.get()
            elif(fn_vlue2=="a10"):
                   val2 = a10.get()
            elif(fn_vlue2=="a11"):
                   val2 = a11.get()
            elif(fn_vlue2=="a12"):
                   val2 = a12.get()
            elif(fn_vlue2=="a13"):
                   val2 = a13.get()
            elif(fn_vlue2=="b1"):
                   val2 = b1.get()
            elif(fn_vlue2=="b2"):
                   val2 = b2.get()
            elif(fn_vlue2=="b3"):
                   val2 = b3.get()
            elif(fn_vlue2=="b4"):
                   val2 = b4.get()
            elif(fn_vlue2=="b5"):
                   val2 = b5.get()
            elif(fn_vlue2=="b6"):
                   val2 = b6.get()
            elif(fn_vlue2=="b7"):
                   val2 = b7.get()
            elif(fn_vlue2=="b8"):
                   val2 = b8.get()
            elif(fn_vlue2=="b9"):
                   val2 = b9.get()
            elif(fn_vlue2=="b10"):
                   val2 = b10.get()
            elif(fn_vlue2=="b11"):
                   val2 = b11.get()
            elif(fn_vlue2=="b12"):
                   val2 = b12.get()
            elif(fn_vlue2=="b13"):
                   val2 = b13.get()
            elif(fn_vlue2=="c1"):
                   val2 = c1.get()
            elif(fn_vlue2=="c2"):
                   val2 = c2.get()
            elif(fn_vlue2=="c3"):
                   val2 = c3.get()
            elif(fn_vlue2=="c4"):
                   val2 = c4.get()
            elif(fn_vlue2=="c5"):
                   val2 = c5.get()
            elif(fn_vlue2=="c6"):
                   val2 = c6.get()
            elif(fn_vlue2=="c7"):
                   val2 = c7.get()
            elif(fn_vlue2=="c8"):
                   val2 = c8.get()
            elif(fn_vlue2=="c9"):
                   val2 = c9.get()
            elif(fn_vlue2=="c10"):
                   val2 = c10.get()
            elif(fn_vlue2=="c11"):
                   val2 = c11.get()
            elif(fn_vlue2=="c12"):
                   val2 = c12.get()
            elif(fn_vlue2=="c13"):
                   val2 = c13.get()
            else:
                   pass
            if(fn_vluem=="+"):
                   va1 = int(val)
                   va2 = int(val2)
                   sum = va1 + va2
                   print(sum)
                   l1 = Label(text=sum, background="#154f69", fg="white", font="bahnschrift 12", width=20)
                   l1.place(x=500, y=85)
            elif(fn_vluem=="-"):
                   va1 = int(val)
                   va2 = int(val2)
                   sum = va1 - va2
                   print(sum)
                   l1 = Label(text=sum, background="#154f69", fg="white", font="bahnschrift 12", width=20)
                   l1.place(x=500, y=85)
            elif(fn_vluem=="*"):
                   va1 = int(val)
                   va2 = int(val2)
                   sum = va1 * va2
                   print(sum)
                   l1 = Label(text=sum, background="#154f69", fg="white", font="bahnschrift 12", width=20)
                   l1.place(x=500, y=85)
            elif(fn_vluem=="/"):
                   va1 = int(val)
                   va2 = int(val2)
                   sum = va1 / va2
                   print(sum)
                   l1 = Label(text=sum, background="#154f69", fg="white", font="bahnschrift 12", width=20)
                   l1.place(x=500, y=85)




# sum
def sum():
      v1 = func1.get()
      v2 = func2.get()

      sign = Label(text="+", background="#154f69", fg="white", font="bahnschrift 10", width=2)
      sign.place(x=741, y=87)

      if(v1=="a1"):
             val = a1.get()
             print(val)
      elif(v1=="a2"):
             val = a2.get()
             print(val)
      elif(v1=="a3"):
             val = a3.get()
             print(val)
      elif(v1=="a4"):
             val = a4.get()
             print(val)
      elif(v1=="a5"):
             val = a5.get()
             print(val)
      elif(v1=="a6"):
             val = a6.get()
             print(val)
      elif(v1=="a7"):
             val = a7.get()
             print(val)
      elif(v1=="a8"):
             val = a8.get()
             print(val)
      elif(v1=="a9"):
             val = a9.get()
             print(val)
      elif(v1=="a10"):
             val = a10.get()
             print(val)
      elif(v1=="a11"):
             val = a11.get()
             print(val)
      elif(v1=="a12"):
             val = a12.get()
             print(val)
      elif(v1=="a13"):
             val = a13.get()
             print(val)
      elif(v1=="b1"):
             val = b1.get()
             print(val)
      elif(v1=="b2"):
             val = b2.get()
             print(val)
      elif(v1=="b3"):
             val = b3.get()
             print(val)
      elif(v1=="b4"):
             val = b4.get()
             print(val)
      elif(v1=="b5"):
             val = b5.get()
             print(val)
      elif(v1=="b6"):
             val = b6.get()
             print(val)
      elif(v1=="b7"):
             val = b7.get()
             print(val)
      elif(v1=="b8"):
             val = b8.get()
             print(val)
      elif(v1=="b9"):
             val = b9.get()
             print(val)
      elif(v1=="b10"):
             val = b10.get()
             print(val)
      elif(v1=="b11"):
             val = b11.get()
             print(val)
      elif(v1=="b12"):
             val = b12.get()
             print(val)
      elif(v1=="b13"):
             val = b13.get()
             print(val)
      elif(v1=="c1"):
             val = c1.get()
             print(val)
      elif(v1=="c2"):
             val = c2.get()
             print(val)
      elif(v1=="c3"):
             val = c3.get()
             print(val)
      elif(v1=="c4"):
             val = c4.get()
             print(val)
      elif(v1=="c5"):
             val = c5.get()
             print(val)
      elif(v1=="c6"):
             val = c6.get()
             print(val)
      elif(v1=="c7"):
             val = c7.get()
             print(val)
      elif(v1=="c8"):
             val = c8.get()
             print(val)
      elif(v1=="c9"):
             val = c9.get()
             print(val)
      elif(v1=="c10"):
             val = c10.get()
             print(val)
      elif(v1=="c11"):
             val = c11.get()
             print(val)
      elif(v1=="c12"):
             val = c12.get()
             print(val)
      elif(v1=="c13"):
             val = c13.get()
             print(val)
      
      else:
             val = v1

      # Value second
      if(v2=="a1"):
             val2 = a1.get()
             print(val2)
      elif(v2=="a2"):
             val2 = a2.get()
             print(val2)
      elif(v2=="a3"):
             val2 = a3.get()
             print(val2)
      elif(v2=="a4"):
             val2 = a4.get()
             print(val2)
      elif(v2=="a5"):
             val2 = a5.get()
             print(val2)
      elif(v2=="a6"):
             val2 = a6.get()
             print(val2)
      elif(v2=="a7"):
             val2 = a7.get()
             print(val2)
      elif(v2=="a8"):
             val2 = a8.get()
             print(val2)
      elif(v2=="a9"):
             val2 = a9.get()
             print(val2)
      elif(v2=="a10"):
             val2 = a10.get()
             print(val2)
      elif(v2=="a11"):
             val2 = a11.get()
             print(val2)
      elif(v2=="a12"):
             val2 = a12.get()
             print(val2)
      elif(v2=="a13"):
             val2 = a13.get()
             print(val2)
      elif(v2=="b1"):
             val2 = b1.get()
             print(val2)
      elif(v2=="b2"):
             val2 = b2.get()
             print(val2)
      elif(v2=="b3"):
             val2 = b3.get()
             print(val2)
      elif(v2=="b4"):
             val2 = b4.get()
             print(val2)
      elif(v2=="b5"):
             val2 = b5.get()
             print(val2)
      elif(v2=="b6"):
             val2 = b6.get()
             print(val2)
      elif(v2=="b7"):
             val2 = b7.get()
             print(val2)
      elif(v2=="b8"):
             val2 = b8.get()
             print(val2)
      elif(v2=="b9"):
             val2 = b9.get()
             print(val2)
      elif(v2=="b10"):
             val2 = b10.get()
             print(val2)
      elif(v2=="b11"):
             val2 = b11.get()
             print(val2)
      elif(v2=="b12"):
             val2 = b12.get()
             print(val2)
      elif(v2=="b13"):
             val2 = b13.get()
             print(val2)
      elif(v2=="c1"):
             val2 = c1.get()
             print(val2)
      elif(v2=="c2"):
             val2 = c2.get()
             print(val2)
      elif(v2=="c3"):
             val2 = c3.get()
             print(val2)
      elif(v2=="c4"):
             val2 = c4.get()
             print(val2)
      elif(v2=="c5"):
             val2 = c5.get()
             print(val2)
      elif(v2=="c6"):
             val2 = c6.get()
             print(val2)
      elif(v2=="c7"):
             val2 = c7.get()
             print(val2)
      elif(v2=="c8"):
             val2 = c8.get()
             print(val2)
      elif(v2=="c9"):
             val2 = c9.get()
             print(val2)
      elif(v2=="c10"):
             val2 = c10.get()
             print(val2)
      elif(v2=="c11"):
             val2 = c11.get()
             print(val2)
      elif(v2=="c12"):
             val2 = c12.get()
             print(val2)
      elif(v2=="c13"):
             val2 = c13.get()
             print(val2)
      else:
             val2 = v2
            
      f_no = int(val)
      s_no = int(val2)
      sum = f_no + s_no
      print(sum)
      l1 = Label(text=sum, background="#154f69", fg="white", font="bahnschrift 12", width=20)
      l1.place(x=500, y=85)

# subtraction
def diff():
      v1 = func1.get()
      v2 = func2.get()

      sign = Label(text="-", background="#154f69", fg="white", font="bahnschrift 10", width=2)
      sign.place(x=741, y=87)

      if(v1=="a1"):
             val = a1.get()
             print(val)
      elif(v1=="a2"):
             val = a2.get()
             print(val)
      elif(v1=="a3"):
             val = a3.get()
             print(val)
      elif(v1=="a4"):
             val = a4.get()
             print(val)
      elif(v1=="a5"):
             val = a5.get()
             print(val)
      elif(v1=="a6"):
             val = a6.get()
             print(val)
      elif(v1=="a7"):
             val = a7.get()
             print(val)
      elif(v1=="a8"):
             val = a8.get()
             print(val)
      elif(v1=="a9"):
             val = a9.get()
             print(val)
      elif(v1=="a10"):
             val = a10.get()
             print(val)
      elif(v1=="a11"):
             val = a11.get()
             print(val)
      elif(v1=="a12"):
             val = a12.get()
             print(val)
      elif(v1=="a13"):
             val = a13.get()
             print(val)
      elif(v1=="b1"):
             val = b1.get()
             print(val)
      elif(v1=="b2"):
             val = b2.get()
             print(val)
      elif(v1=="b3"):
             val = b3.get()
             print(val)
      elif(v1=="b4"):
             val = b4.get()
             print(val)
      elif(v1=="b5"):
             val = b5.get()
             print(val)
      elif(v1=="b6"):
             val = b6.get()
             print(val)
      elif(v1=="b7"):
             val = b7.get()
             print(val)
      elif(v1=="b8"):
             val = b8.get()
             print(val)
      elif(v1=="b9"):
             val = b9.get()
             print(val)
      elif(v1=="b10"):
             val = b10.get()
             print(val)
      elif(v1=="b11"):
             val = b11.get()
             print(val)
      elif(v1=="b12"):
             val = b12.get()
             print(val)
      elif(v1=="b13"):
             val = b13.get()
             print(val)
      elif(v1=="c1"):
             val = c1.get()
             print(val)
      elif(v1=="c2"):
             val = c2.get()
             print(val)
      elif(v1=="c3"):
             val = c3.get()
             print(val)
      elif(v1=="c4"):
             val = c4.get()
             print(val)
      elif(v1=="c5"):
             val = c5.get()
             print(val)
      elif(v1=="c6"):
             val = c6.get()
             print(val)
      elif(v1=="c7"):
             val = c7.get()
             print(val)
      elif(v1=="c8"):
             val = c8.get()
             print(val)
      elif(v1=="c9"):
             val = c9.get()
             print(val)
      elif(v1=="c10"):
             val = c10.get()
             print(val)
      elif(v1=="c11"):
             val = c11.get()
             print(val)
      elif(v1=="c12"):
             val = c12.get()
             print(val)
      elif(v1=="c13"):
             val = c13.get()
             print(val)
      
      else:
             val = v1

      # Value second
      if(v2=="a1"):
             val2 = a1.get()
             print(val2)
      elif(v2=="a2"):
             val2 = a2.get()
             print(val2)
      elif(v2=="a3"):
             val2 = a3.get()
             print(val2)
      elif(v2=="a4"):
             val2 = a4.get()
             print(val2)
      elif(v2=="a5"):
             val2 = a5.get()
             print(val2)
      elif(v2=="a6"):
             val2 = a6.get()
             print(val2)
      elif(v2=="a7"):
             val2 = a7.get()
             print(val2)
      elif(v2=="a8"):
             val2 = a8.get()
             print(val2)
      elif(v2=="a9"):
             val2 = a9.get()
             print(val2)
      elif(v2=="a10"):
             val2 = a10.get()
             print(val2)
      elif(v2=="a11"):
             val2 = a11.get()
             print(val2)
      elif(v2=="a12"):
             val2 = a12.get()
             print(val2)
      elif(v2=="a13"):
             val2 = a13.get()
             print(val2)
      elif(v2=="b1"):
             val2 = b1.get()
             print(val2)
      elif(v2=="b2"):
             val2 = b2.get()
             print(val2)
      elif(v2=="b3"):
             val2 = b3.get()
             print(val2)
      elif(v2=="b4"):
             val2 = b4.get()
             print(val2)
      elif(v2=="b5"):
             val2 = b5.get()
             print(val2)
      elif(v2=="b6"):
             val2 = b6.get()
             print(val2)
      elif(v2=="b7"):
             val2 = b7.get()
             print(val2)
      elif(v2=="b8"):
             val2 = b8.get()
             print(val2)
      elif(v2=="b9"):
             val2 = b9.get()
             print(val2)
      elif(v2=="b10"):
             val2 = b10.get()
             print(val2)
      elif(v2=="b11"):
             val2 = b11.get()
             print(val2)
      elif(v2=="b12"):
             val2 = b12.get()
             print(val2)
      elif(v2=="b13"):
             val2 = b13.get()
             print(val2)
      elif(v2=="c1"):
             val2 = c1.get()
             print(val2)
      elif(v2=="c2"):
             val2 = c2.get()
             print(val2)
      elif(v2=="c3"):
             val2 = c3.get()
             print(val2)
      elif(v2=="c4"):
             val2 = c4.get()
             print(val2)
      elif(v2=="c5"):
             val2 = c5.get()
             print(val2)
      elif(v2=="c6"):
             val2 = c6.get()
             print(val2)
      elif(v2=="c7"):
             val2 = c7.get()
             print(val2)
      elif(v2=="c8"):
             val2 = c8.get()
             print(val2)
      elif(v2=="c9"):
             val2 = c9.get()
             print(val2)
      elif(v2=="c10"):
             val2 = c10.get()
             print(val2)
      elif(v2=="c11"):
             val2 = c11.get()
             print(val2)
      elif(v2=="c12"):
             val2 = c12.get()
             print(val2)
      elif(v2=="c13"):
             val2 = c13.get()
             print(val2)
      else:
             val2 = v2
            
      f_no = int(val)
      s_no = int(val2)
      sum = f_no - s_no
      print(sum)
      l1 = Label(text=sum, background="#154f69", fg="white", font="bahnschrift 12", width=20)
      l1.place(x=500, y=85)
      
# count
def coun():
      v1 = func1.get()
      v2 = func2.get()

      sign = Label(text="and", background="#154f69", fg="white", font="bahnschrift 10")
      sign.place(x=738, y=87)

      if(v1=="a1"):
             val = a1.get()
             print(val)
      elif(v1=="a2"):
             val = a2.get()
             print(val)
      elif(v1=="a3"):
             val = a3.get()
             print(val)
      elif(v1=="a4"):
             val = a4.get()
             print(val)
      elif(v1=="a5"):
             val = a5.get()
             print(val)
      elif(v1=="a6"):
             val = a6.get()
             print(val)
      elif(v1=="a7"):
             val = a7.get()
             print(val)
      elif(v1=="a8"):
             val = a8.get()
             print(val)
      elif(v1=="a9"):
             val = a9.get()
             print(val)
      elif(v1=="a10"):
             val = a10.get()
             print(val)
      elif(v1=="a11"):
             val = a11.get()
             print(val)
      elif(v1=="a12"):
             val = a12.get()
             print(val)
      elif(v1=="a13"):
             val = a13.get()
             print(val)
      elif(v1=="b1"):
             val = b1.get()
             print(val)
      elif(v1=="b2"):
             val = b2.get()
             print(val)
      elif(v1=="b3"):
             val = b3.get()
             print(val)
      elif(v1=="b4"):
             val = b4.get()
             print(val)
      elif(v1=="b5"):
             val = b5.get()
             print(val)
      elif(v1=="b6"):
             val = b6.get()
             print(val)
      elif(v1=="b7"):
             val = b7.get()
             print(val)
      elif(v1=="b8"):
             val = b8.get()
             print(val)
      elif(v1=="b9"):
             val = b9.get()
             print(val)
      elif(v1=="b10"):
             val = b10.get()
             print(val)
      elif(v1=="b11"):
             val = b11.get()
             print(val)
      elif(v1=="b12"):
             val = b12.get()
             print(val)
      elif(v1=="b13"):
             val = b13.get()
             print(val)
      elif(v1=="c1"):
             val = c1.get()
             print(val)
      elif(v1=="c2"):
             val = c2.get()
             print(val)
      elif(v1=="c3"):
             val = c3.get()
             print(val)
      elif(v1=="c4"):
             val = c4.get()
             print(val)
      elif(v1=="c5"):
             val = c5.get()
             print(val)
      elif(v1=="c6"):
             val = c6.get()
             print(val)
      elif(v1=="c7"):
             val = c7.get()
             print(val)
      elif(v1=="c8"):
             val = c8.get()
             print(val)
      elif(v1=="c9"):
             val = c9.get()
             print(val)
      elif(v1=="c10"):
             val = c10.get()
             print(val)
      elif(v1=="c11"):
             val = c11.get()
             print(val)
      elif(v1=="c12"):
             val = c12.get()
             print(val)
      elif(v1=="c13"):
             val = c13.get()
             print(val)
      
      else:
             val = v1

      # Value second
      if(v2=="a1"):
             val2 = a1.get()
             print(val2)
      elif(v2=="a2"):
             val2 = a2.get()
             print(val2)
      elif(v2=="a3"):
             val2 = a3.get()
             print(val2)
      elif(v2=="a4"):
             val2 = a4.get()
             print(val2)
      elif(v2=="a5"):
             val2 = a5.get()
             print(val2)
      elif(v2=="a6"):
             val2 = a6.get()
             print(val2)
      elif(v2=="a7"):
             val2 = a7.get()
             print(val2)
      elif(v2=="a8"):
             val2 = a8.get()
             print(val2)
      elif(v2=="a9"):
             val2 = a9.get()
             print(val2)
      elif(v2=="a10"):
             val2 = a10.get()
             print(val2)
      elif(v2=="a11"):
             val2 = a11.get()
             print(val2)
      elif(v2=="a12"):
             val2 = a12.get()
             print(val2)
      elif(v2=="a13"):
             val2 = a13.get()
             print(val2)
      elif(v2=="b1"):
             val2 = b1.get()
             print(val2)
      elif(v2=="b2"):
             val2 = b2.get()
             print(val2)
      elif(v2=="b3"):
             val2 = b3.get()
             print(val2)
      elif(v2=="b4"):
             val2 = b4.get()
             print(val2)
      elif(v2=="b5"):
             val2 = b5.get()
             print(val2)
      elif(v2=="b6"):
             val2 = b6.get()
             print(val2)
      elif(v2=="b7"):
             val2 = b7.get()
             print(val2)
      elif(v2=="b8"):
             val2 = b8.get()
             print(val2)
      elif(v2=="b9"):
             val2 = b9.get()
             print(val2)
      elif(v2=="b10"):
             val2 = b10.get()
             print(val2)
      elif(v2=="b11"):
             val2 = b11.get()
             print(val2)
      elif(v2=="b12"):
             val2 = b12.get()
             print(val2)
      elif(v2=="b13"):
             val2 = b13.get()
             print(val2)
      elif(v2=="c1"):
             val2 = c1.get()
             print(val2)
      elif(v2=="c2"):
             val2 = c2.get()
             print(val2)
      elif(v2=="c3"):
             val2 = c3.get()
             print(val2)
      elif(v2=="c4"):
             val2 = c4.get()
             print(val2)
      elif(v2=="c5"):
             val2 = c5.get()
             print(val2)
      elif(v2=="c6"):
             val2 = c6.get()
             print(val2)
      elif(v2=="c7"):
             val2 = c7.get()
             print(val2)
      elif(v2=="c8"):
             val2 = c8.get()
             print(val2)
      elif(v2=="c9"):
             val2 = c9.get()
             print(val2)
      elif(v2=="c10"):
             val2 = c10.get()
             print(val2)
      elif(v2=="c11"):
             val2 = c11.get()
             print(val2)
      elif(v2=="c12"):
             val2 = c12.get()
             print(val2)
      elif(v2=="c13"):
             val2 = c13.get()
             print(val2)
      else:
             val2 = v2
            
      f_no = val
      s_no = val2
      sum = [f_no + s_no]
      for i in sum:
             print(len(i))
      l1 = Label(text=len(i), background="#154f69", fg="white", font="bahnschrift 12", width=20)
      l1.place(x=500, y=85)

# percentage
def perc():
      v1 = func1.get()
      v2 = func2.get()

      sign = Label(text="/", background="#154f69", fg="white", font="bahnschrift 10", width=2)
      sign.place(x=741, y=87)

      if(v1=="a1"):
             val = a1.get()
             print(val)
      elif(v1=="a2"):
             val = a2.get()
             print(val)
      elif(v1=="a3"):
             val = a3.get()
             print(val)
      elif(v1=="a4"):
             val = a4.get()
             print(val)
      elif(v1=="a5"):
             val = a5.get()
             print(val)
      elif(v1=="a6"):
             val = a6.get()
             print(val)
      elif(v1=="a7"):
             val = a7.get()
             print(val)
      elif(v1=="a8"):
             val = a8.get()
             print(val)
      elif(v1=="a9"):
             val = a9.get()
             print(val)
      elif(v1=="a10"):
             val = a10.get()
             print(val)
      elif(v1=="a11"):
             val = a11.get()
             print(val)
      elif(v1=="a12"):
             val = a12.get()
             print(val)
      elif(v1=="a13"):
             val = a13.get()
             print(val)
      elif(v1=="b1"):
             val = b1.get()
             print(val)
      elif(v1=="b2"):
             val = b2.get()
             print(val)
      elif(v1=="b3"):
             val = b3.get()
             print(val)
      elif(v1=="b4"):
             val = b4.get()
             print(val)
      elif(v1=="b5"):
             val = b5.get()
             print(val)
      elif(v1=="b6"):
             val = b6.get()
             print(val)
      elif(v1=="b7"):
             val = b7.get()
             print(val)
      elif(v1=="b8"):
             val = b8.get()
             print(val)
      elif(v1=="b9"):
             val = b9.get()
             print(val)
      elif(v1=="b10"):
             val = b10.get()
             print(val)
      elif(v1=="b11"):
             val = b11.get()
             print(val)
      elif(v1=="b12"):
             val = b12.get()
             print(val)
      elif(v1=="b13"):
             val = b13.get()
             print(val)
      elif(v1=="c1"):
             val = c1.get()
             print(val)
      elif(v1=="c2"):
             val = c2.get()
             print(val)
      elif(v1=="c3"):
             val = c3.get()
             print(val)
      elif(v1=="c4"):
             val = c4.get()
             print(val)
      elif(v1=="c5"):
             val = c5.get()
             print(val)
      elif(v1=="c6"):
             val = c6.get()
             print(val)
      elif(v1=="c7"):
             val = c7.get()
             print(val)
      elif(v1=="c8"):
             val = c8.get()
             print(val)
      elif(v1=="c9"):
             val = c9.get()
             print(val)
      elif(v1=="c10"):
             val = c10.get()
             print(val)
      elif(v1=="c11"):
             val = c11.get()
             print(val)
      elif(v1=="c12"):
             val = c12.get()
             print(val)
      elif(v1=="c13"):
             val = c13.get()
             print(val)
      
      else:
             val = v1

      # Value second
      if(v2=="a1"):
             val2 = a1.get()
             print(val2)
      elif(v2=="a2"):
             val2 = a2.get()
             print(val2)
      elif(v2=="a3"):
             val2 = a3.get()
             print(val2)
      elif(v2=="a4"):
             val2 = a4.get()
             print(val2)
      elif(v2=="a5"):
             val2 = a5.get()
             print(val2)
      elif(v2=="a6"):
             val2 = a6.get()
             print(val2)
      elif(v2=="a7"):
             val2 = a7.get()
             print(val2)
      elif(v2=="a8"):
             val2 = a8.get()
             print(val2)
      elif(v2=="a9"):
             val2 = a9.get()
             print(val2)
      elif(v2=="a10"):
             val2 = a10.get()
             print(val2)
      elif(v2=="a11"):
             val2 = a11.get()
             print(val2)
      elif(v2=="a12"):
             val2 = a12.get()
             print(val2)
      elif(v2=="a13"):
             val2 = a13.get()
             print(val2)
      elif(v2=="b1"):
             val2 = b1.get()
             print(val2)
      elif(v2=="b2"):
             val2 = b2.get()
             print(val2)
      elif(v2=="b3"):
             val2 = b3.get()
             print(val2)
      elif(v2=="b4"):
             val2 = b4.get()
             print(val2)
      elif(v2=="b5"):
             val2 = b5.get()
             print(val2)
      elif(v2=="b6"):
             val2 = b6.get()
             print(val2)
      elif(v2=="b7"):
             val2 = b7.get()
             print(val2)
      elif(v2=="b8"):
             val2 = b8.get()
             print(val2)
      elif(v2=="b9"):
             val2 = b9.get()
             print(val2)
      elif(v2=="b10"):
             val2 = b10.get()
             print(val2)
      elif(v2=="b11"):
             val2 = b11.get()
             print(val2)
      elif(v2=="b12"):
             val2 = b12.get()
             print(val2)
      elif(v2=="b13"):
             val2 = b13.get()
             print(val2)
      elif(v2=="c1"):
             val2 = c1.get()
             print(val2)
      elif(v2=="c2"):
             val2 = c2.get()
             print(val2)
      elif(v2=="c3"):
             val2 = c3.get()
             print(val2)
      elif(v2=="c4"):
             val2 = c4.get()
             print(val2)
      elif(v2=="c5"):
             val2 = c5.get()
             print(val2)
      elif(v2=="c6"):
             val2 = c6.get()
             print(val2)
      elif(v2=="c7"):
             val2 = c7.get()
             print(val2)
      elif(v2=="c8"):
             val2 = c8.get()
             print(val2)
      elif(v2=="c9"):
             val2 = c9.get()
             print(val2)
      elif(v2=="c10"):
             val2 = c10.get()
             print(val2)
      elif(v2=="c11"):
             val2 = c11.get()
             print(val2)
      elif(v2=="c12"):
             val2 = c12.get()
             print(val2)
      elif(v2=="c13"):
             val2 = c13.get()
             print(val2)
      else:
             val2 = v2
            
      f_no = int(val)
      s_no = int(val2)
      sum = f_no*100/s_no
      print(sum)
      l1 = Label(text=sum, background="#154f69", fg="white", font="bahnschrift 12", width=20)
      l1.place(x=500, y=85)


def cancel():
       prompt.place_forget()
       msg.place_forget()
       ok.place_forget()
       no.place_forget()
       can.place_forget()


def nwFile():
       prompt.place(x=400, y=160)
       msg.place(x=460, y=190)
       ok.place(x=480, y=280)
       no.place(x=540, y=280)
       can.place(x=650, y=280)



def hide():
       base.place_forget()
       nav.place_forget()
       cr_new.place_forget()
       opn.place_forget()
       bck.place_forget()
       qte.place_forget()
       save.place_forget()
       prm.place_forget()
       msg2.place_forget()
       ok2.place_forget()
       bn_hm.place(x=70, y=23)
       dsn.place(x=118, y=23)
       fml.place(x=164, y=23)
       ln.place(x=0, y=43)
       ttl_nm = Label(ttl_bar, text=f_nm, fg="white", font="bahnschrift 10", background="#24546a")
       ttl_nm.place(x=300, y=2)
       bn_hm.place(x=70, y=23)
       dsn.place(x=118, y=23)
       fml.place(x=164, y=23)
       

def show():
        base.place(x=0, y=0)
        nav.place(x=0, y=0)
        cr_new.place(x=0, y=90)
        opn.place(x=0, y=210)
        bck.place(x=0, y=30)
        qte.place(x=0, y=560)
        save.place(x=0, y=160)
        bn_hm.place_forget()
        dsn.place_forget()
        fml.place_forget()
        ln.place_forget()



def fle():
       area = Frame(height=1100, width=2000, background="white")
       area.place(x=0, y=0)
       ttl_br = Frame(height=130, width=2000, background="#326a83")
       ttl_br.place(x=0, y=20)
       back = Button(text="Menu", height=0, width=0, background="#326a83", fg="white", font="bahnschrift 12", border=0, command=show)
       back.place(x=0, y=20)


       # Functions: -

       func1 = Entry(width=4)
       func1.place(x=700, y=90)
       func2 = Entry(width=4)
       func2.place(x=760, y=90)

       sm = Button(text="SUM", background="#326a83", fg="white", border=0, font="bahnschrift 10", command=sum)
       dif = Button(text="DIFFERENCE", background="#326a83", fg="white", border=0, font="bahnschrift 10", command=diff)
       cnt = Button(text="COUNT", background="#326a83", fg="white", border=0, font="bahnschrift 10", command=coun)
       per = Button(text="PERCENT", background="#326a83", fg="white", border=0, font="bahnschrift 10", command=perc)
       sm.place(x=810, y=87) 
       dif.place(x=850, y=87) 
       cnt.place(x=940, y=87) 
       per.place(x=995, y=87) 

       # Rows And Columns: -
       # Row A--
       doc = Frame(height=800, width=2000, background="white")
       doc.place(x=0, y=150)


       a1 = Entry(doc, width=6, border=2)
       a2 = Entry(doc, width=6, border=2)
       a3 = Entry(doc, width=6, border=2)
       a4 = Entry(doc, width=6, border=2)
       a5 = Entry(doc, width=6, border=2)
       a6 = Entry(doc, width=6, border=2)
       a7 = Entry(doc, width=6, border=2)
       a8 = Entry(doc, width=6, border=2)
       a9 = Entry(doc, width=6, border=2)
       a10 = Entry(doc, width=6, border=2)
       a11 = Entry(doc, width=6, border=2)
       a12 = Entry(doc, width=6, border=2)
       a13 = Entry(doc, width=6, border=2)
       a1.grid(row=1, column=1)
       a2.grid(row=2, column=1)
       a3.grid(row=3, column=1)
       a4.grid(row=4, column=1)
       a5.grid(row=5, column=1)
       a6.grid(row=6, column=1)
       a7.grid(row=8, column=1)
       a8.grid(row=8, column=1)
       a9.grid(row=9, column=1)
       a10.grid(row=10, column=1)
       a11.grid(row=11, column=1)
       a12.grid(row=12, column=1)
       a13.grid(row=13, column=1)
       # Row-- B
       b1 = Entry(doc, width=6, border=2)
       b2 = Entry(doc, width=6, border=2)
       b3 = Entry(doc, width=6, border=2)
       b4 = Entry(doc, width=6, border=2)
       b5 = Entry(doc, width=6, border=2)
       b6 = Entry(doc, width=6, border=2)
       b7 = Entry(doc, width=6, border=2)
       b8 = Entry(doc, width=6, border=2)
       b9 = Entry(doc, width=6, border=2)
       b10 = Entry(doc, width=6, border=2)
       b11 = Entry(doc, width=6, border=2)
       b12 = Entry(doc, width=6, border=2)
       b13 = Entry(doc, width=6, border=2)
       b1.grid(row=1, column=2)
       b2.grid(row=2, column=2)
       b3.grid(row=3, column=2)
       b4.grid(row=4, column=2)
       b5.grid(row=5, column=2)
       b6.grid(row=6, column=2)
       b7.grid(row=8, column=2)
       b8.grid(row=8, column=2)
       b9.grid(row=9, column=2)
       b10.grid(row=10, column=2)
       b11.grid(row=11, column=2)
       b12.grid(row=12, column=2)
       b13.grid(row=13, column=2)

       # Row-- C
       c1 = Entry(doc, width=6, border=2)
       c2 = Entry(doc, width=6, border=2)
       c3 = Entry(doc, width=6, border=2)
       c4 = Entry(doc, width=6, border=2)
       c5 = Entry(doc, width=6, border=2)
       c6 = Entry(doc, width=6, border=2)
       c7 = Entry(doc, width=6, border=2)
       c8 = Entry(doc, width=6, border=2)
       c9 = Entry(doc, width=6, border=2)
       c10 = Entry(doc, width=6, border=2)
       c11 = Entry(doc, width=6, border=2)
       c12 = Entry(doc, width=6, border=2)
       c13 = Entry(doc, width=6, border=2)
       c1.grid(row=1, column=3)
       c2.grid(row=2, column=3)
       c3.grid(row=3, column=3)
       c4.grid(row=4, column=3)
       c5.grid(row=5, column=3)
       c6.grid(row=6, column=3)
       c7.grid(row=8, column=3)
       c8.grid(row=8, column=3)
       c9.grid(row=9, column=3)
       c10.grid(row=10, column=3)
       c11.grid(row=11, column=3)
       c12.grid(row=12, column=3)
       c13.grid(row=13, column=3)


       fr_mla = Entry(width=40, border=0)
       fr_mla.place(x=200, y=85)
       entr = Button(text="Enter", command=fuctns)
       entr.pack()

       # File Menu
       base = Frame(height=1100, width=2000, background="white")
       nav = Frame(base, background="#326a83", height="1100", width="240")
       bck = Button(nav, text="Back", background="#326a83", fg="white", height=2, width=26, border=0, font="bahnschrift 12", command=hide)
       cr_new = Button(nav, text="Create New File", background="#326a83", fg="white", height=2, width=26, border=0, font="bahnschrift 12", command=nwFile)
       qte = Button(text="Exit", background="#326a83", fg="white", font="bahnschrift 12", border=0, width=26)
       save = Button(text="Save", background="#326a83", fg="white", command=saveFile, font="bahnschrift 12", border=0, width=26)


       # prompts
       prompt = Frame(height=180, width=390, background="#326a83")
       msg = Label(text="Do you really want to Save this file?\n Click \'Don\'t save\' to create New file..", fg="white", background="#326a83", font="bahnschrift 12")
       ok = Button(text="Save", fg="white", border=0, background="#326a83", font="bahnschrift 12")
       no = Button(text="Don't Save", fg="white", border=0, background="#326a83", font="bahnschrift 12", command=fle)
       can = Button(text="Cancel", fg="white", border=0, background="#326a83", font="bahnschrift 12", command=cancel)



area = Frame(height=1100, width=2000, background="white")
area.place(x=0, y=0)
ttl_br = Frame(height=130, width=2000, background="#326a83")
ttl_br.place(x=0, y=20)
back = Button(text="Menu", height=0, width=0, background="#326a83", fg="white", font="bahnschrift 12", border=0, command=show)
back.place(x=4, y=18)
lnm = Frame(height=110, width=2000, background="#154f69")
lnm.place(x=0, y=43)


# Functions: -

func1 = Entry(width=4)
func1.place(x=700, y=90)
func2 = Entry(width=4)
func2.place(x=772, y=90)

sm = Button(text="SUM", background="#154f69", fg="white", border=0, font="bahnschrift 10", command=sum)
dif = Button(text="DIFFERENCE", background="#154f69", fg="white", border=0, font="bahnschrift 10", command=diff)
cnt = Button(text="COUNT", background="#154f69", fg="white", border=0, font="bahnschrift 10", command=coun)
per = Button(text="PERCENT", background="#154f69", fg="white", border=0, font="bahnschrift 10", command=perc)
sm.place(x=810, y=87) 
dif.place(x=850, y=87) 
cnt.place(x=940, y=87) 
per.place(x=995, y=87) 

# Rows And Columns: -
# Row A--
doc = Frame(height=800, width=2000, background="white")
doc.place(x=0, y=150)


a1 = Entry(doc, width=6, border=2)
a2 = Entry(doc, width=6, border=2)
a3 = Entry(doc, width=6, border=2)
a4 = Entry(doc, width=6, border=2)
a5 = Entry(doc, width=6, border=2)
a6 = Entry(doc, width=6, border=2)
a7 = Entry(doc, width=6, border=2)
a8 = Entry(doc, width=6, border=2)
a9 = Entry(doc, width=6, border=2)
a10 = Entry(doc, width=6, border=2)
a11 = Entry(doc, width=6, border=2)
a12 = Entry(doc, width=6, border=2)
a13 = Entry(doc, width=6, border=2)
a1.grid(row=1, column=1)
a2.grid(row=2, column=1)
a3.grid(row=3, column=1)
a4.grid(row=4, column=1)
a5.grid(row=5, column=1)
a6.grid(row=6, column=1)
a7.grid(row=8, column=1)
a8.grid(row=8, column=1)
a9.grid(row=9, column=1)
a10.grid(row=10, column=1)
a11.grid(row=11, column=1)
a12.grid(row=12, column=1)
a13.grid(row=13, column=1)
# Row-- B
b1 = Entry(doc, width=6, border=2)
b2 = Entry(doc, width=6, border=2)
b3 = Entry(doc, width=6, border=2)
b4 = Entry(doc, width=6, border=2)
b5 = Entry(doc, width=6, border=2)
b6 = Entry(doc, width=6, border=2)
b7 = Entry(doc, width=6, border=2)
b8 = Entry(doc, width=6, border=2)
b9 = Entry(doc, width=6, border=2)
b10 = Entry(doc, width=6, border=2)
b11 = Entry(doc, width=6, border=2)
b12 = Entry(doc, width=6, border=2)
b13 = Entry(doc, width=6, border=2)
b1.grid(row=1, column=2)
b2.grid(row=2, column=2)
b3.grid(row=3, column=2)
b4.grid(row=4, column=2)
b5.grid(row=5, column=2)
b6.grid(row=6, column=2)
b7.grid(row=8, column=2)
b8.grid(row=8, column=2)
b9.grid(row=9, column=2)
b10.grid(row=10, column=2)
b11.grid(row=11, column=2)
b12.grid(row=12, column=2)
b13.grid(row=13, column=2)

# Row-- C
c1 = Entry(doc, width=6, border=2)
c2 = Entry(doc, width=6, border=2)
c3 = Entry(doc, width=6, border=2)
c4 = Entry(doc, width=6, border=2)
c5 = Entry(doc, width=6, border=2)
c6 = Entry(doc, width=6, border=2)
c7 = Entry(doc, width=6, border=2)
c8 = Entry(doc, width=6, border=2)
c9 = Entry(doc, width=6, border=2)
c10 = Entry(doc, width=6, border=2)
c11 = Entry(doc, width=6, border=2)
c12 = Entry(doc, width=6, border=2)
c13 = Entry(doc, width=6, border=2)
c1.grid(row=1, column=3)
c2.grid(row=2, column=3)
c3.grid(row=3, column=3)
c4.grid(row=4, column=3)
c5.grid(row=5, column=3)
c6.grid(row=6, column=3)
c7.grid(row=8, column=3)
c8.grid(row=8, column=3)
c9.grid(row=9, column=3)
c10.grid(row=10, column=3)
c11.grid(row=11, column=3)
c12.grid(row=12, column=3)
c13.grid(row=13, column=3)



fr_mla = Entry(width=40, border=0)
fr_mla.place(x=200, y=85)
entr = Button(text="Run", command=fuctns, fg="white", border=2, background="#326a83", font="bahnschrift 10", height=1)
entr.place(x=450, y=80)

# File Menu
base = Frame(height=1100, width=2000, background="white")
nav = Frame(base, background="#326a83", height="1100", width="240")
bck = Button(nav, text="Back", background="#326a83", fg="white", height=2, width=26, border=0, font="bahnschrift 12", command=hide)
cr_new = Button(nav, text="Create New File", background="#326a83", fg="white", height=2, width=26, border=0, font="bahnschrift 12", command=nwFile)
opn = Button(nav, text="Open", background="#326a83", fg="white", height=2, width=26, border=0, font="bahnschrift 12", command=load)
qte = Button(text="Exit", background="#326a83", fg="white", font="bahnschrift 12", border=0, width=26)
save = Button(text="Save", background="#326a83", fg="white", command=saveFile, font="bahnschrift 12", border=0, width=26)


# prompts
prompt = Frame(height=180, width=390, background="#326a83")
msg = Label(text="Do you really want to Save this file?\n Click \'Don\'t save\' to create New file..", fg="white", background="#326a83", font="bahnschrift 12")
ok = Button(text="Save", fg="white", border=0, background="#326a83", font="bahnschrift 12", command=saveFile)
no = Button(text="Don't Save", fg="white", border=0, background="#326a83", font="bahnschrift 12", command=fle)
can = Button(text="Cancel", fg="white", border=0, background="#326a83", font="bahnschrift 12", command=cancel)


# errors
prm = Frame(height=130, width=490, background="#326a83")
msg2 = Label(text="Error In Formula, a foumula must be start from the sign \'=\'", fg="white", background="#326a83", font="bahnschrift 12")
ok2 = Button(text="Ok", fg="white", border=0, background="#326a83", font="bahnschrift 12", command=hide)

# title bar
ttl_bar = Frame(height=23, width=2000, background="#24546a")
ttl_bar.place(x=0, y=0)
ttl_nm = Label(ttl_bar, text=f_nm, fg="white", font="bahnschrift 10", background="#24546a")
ttl_nm.place(x=300, y=2)

bn_hm = Button(text="Home", fg="white", font="bahnschrift 9", background="#326a83", border=0, height=1, width=6)
bn_hm.place(x=70, y=23)
dsn = Button(text="Design", fg="white", font="bahnschrift 9", background="#326a83", border=0, height=1, width=6)
dsn.place(x=118, y=23)
fml = Button(text="Formula", fg="white", font="bahnschrift 9", background="#326a83", border=0, height=1, width=8)
fml.place(x=164, y=23)
ln = Frame(height=1, width=2000, background="#154f69")
ln.place(x=0, y=46)

root.mainloop()