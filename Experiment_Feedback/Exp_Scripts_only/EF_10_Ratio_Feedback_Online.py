### -------------------- PreScript ---------------------------------------------- ###


from System import Array
from System.Diagnostics import Process

# calculate ratio
def ArrayDiv(a, b):
    out = Array.CreateInstance(float, len(a))
    outstr = ''
    for i in range(0, len(a)):
        out[i] = a[i] / b[i]
        outstr = outstr + str(round(out[i], 2)) + '\t'
    return out, outstr

filename = ZenService.Experiment.ImageFileName[:-4] + '_Log.txt'
exeloc = 'python'
script = r'C:\TFS\Doc\3-ZIS\3-Development\Discussions\ExpFeedback\DVD_2_5\Python_Scripts\dynamic_MeanROI_Cells.py'
cmd = script + ' -f ' + filename


## start Python Option 1
#ZenService.Xtra.System.ExecuteExternalProgram(script, ' -f ' + filename)

## start Python Option 2
app = Process();
app.StartInfo.FileName = exeloc
app.StartInfo.Arguments = cmd
app.Start()




### -------------------- LoopScript --------------------------------------------- ###


frame = ZenService.Analysis.Cells.ImageIndexTime

# get intensities for all cells
int340 = ZenService.Analysis.Cell.IntensityMean_F2
int380 = ZenService.Analysis.Cell.IntensityMean_F2C

# calculate intensity ratio
ratio, ratiostr = ArrayDiv(int380, int340)

logfile = ZenService.Xtra.System.AppendLogLine(str(frame) + '\t' + ratiostr)


### -------------------- PostScript --------------------------------------------- ###


ZenService.Xtra.System.ExecuteExternalProgram(r"C:\Program Files\Notepad++\notepad++.exe", logfile)