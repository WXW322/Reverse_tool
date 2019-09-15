from splitter.VE_spliter import splitter
from common.measure_tool.MessaSplitMeasure import MessageSplitMeasure
from Config.modbus import modbus
from Config.iec104 import iec104
from common.readdata import *
import sys
import time

def FrequentTest(Messages):
    vespliter = splitter()
    FinalBorders = vespliter.split_by_frequent(Messages)
    ModbusConfig = modbus()
    RightBorders = [ModbusConfig.GetMessageBorder(Message) for Message in Messages]
    MeasureTool = MessageSplitMeasure()
    print(MeasureTool.Measure(RightBorders, FinalBorders))

def EntryTest(Messages):
    vespliter = splitter()
    FinalBorders = vespliter.split_by_entry(Messages)
    ModbusConfig = modbus()
    RightBorders = [ModbusConfig.GetMessageBorder(Message) for Message in Messages]
    MeasureTool = MessageSplitMeasure()
    print(MeasureTool.Measure(RightBorders, FinalBorders))

def OrderTest(Messages):
    vespliter = splitter()
    FinalBorders = vespliter.SplitByOrder(Messages)
    print(FinalBorders[0])
    ModbusConfig = modbus()
    RightBorders = [ModbusConfig.GetMessageBorder(Message) for Message in Messages]
    MeasureTool = MessageSplitMeasure()
    print(MeasureTool.Measure(RightBorders, FinalBorders))

def OrderMergeTest(Messages, VoterA, VoterB):
    vespliter = splitter()
    FinalBorders = vespliter.CombineSplitBorders(Messages, VoterA, VoterB)
    print(FinalBorders[0])
    ModbusConfig = modbus()
    RightBorders = [ModbusConfig.GetMessageBorder(Message) for Message in Messages]
    MeasureTool = MessageSplitMeasure()
    print(MeasureTool.Measure(RightBorders, FinalBorders))



if __name__ == '__main__':
    raw_messages = read_multity_dirs(["/home/wxw/data/iec104"])
    pure_datas = get_puredatas(raw_messages)
    #EntryTest(pure_datas)
    #FrequentTest(pure_datas)
    StartTime = time.time()
    OrderMergeTest(pure_datas, 'order', 'entry')
    #OrderTest(pure_datas)
    EndTime = time.time()
    print(EndTime - StartTime)
    #OrderMergeTest(pure_datas, 'frequent', 'entry')


