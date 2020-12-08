import subprocess
import pickle
import os

def hash(baselineFile, targetPath, tmpFile):
        try:
            ''' POWERSHELL EXECUTION SECTION '''
            print("\n\tOBTENCION DE HASHES")
            command = "powershell -ExecutionPolicy ByPass -File HashAcquire.ps1 -TargetFolder "+\
                      targetPath + " -ResultFile " + tmpFile
            print(command)
            powerShellResult = subprocess.run(command, stdout=subprocess.PIPE)
            if powerShellResult.stderr == None:
                print("Conexión con Powershell exitosa")
                ''' DICTIONARY CREATION SECTION '''
                baseDict = {}
                with open(tmpFile, 'r') as inFile:
                        for eachLine in inFile:
                            lineList = eachLine.split()
                            if len(lineList) == 2:
                                    hashValue = lineList[0]
                                    fileName  = lineList[1]
                                    baseDict[hashValue] = fileName
                            else:
                                continue
                with open(baselineFile, 'wb') as outFile:
                    pickle.dump(baseDict, outFile)
                    print("Baseline: ", baselineFile, " Created with:",
                            "{:,}".format(len(baseDict)), "Records")
                    print("Script Terminado Exitosamente")
            else:
                print("PowerShell Error:", p.stderr)
        except Exception as err:
            print ("No pudo crearse el archivo output: "+str(err))
            quit()
        return tmpFile
