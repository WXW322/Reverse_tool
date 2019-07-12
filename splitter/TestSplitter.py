from splitter.VE_spliter import splitter
from common.measure_tool.MessaSplitMeasure import MessageSplitMeasure
from Config.modbus import modbus
from common.readdata import *
import sys

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
    raw_messages = read_multity_dirs(["/home/wxw/data/modbusdata", "/home/wxw/data/modbusgithub"])
    pure_datas = get_puredatas(raw_messages)
    #EntryTest(pure_datas)
    #FrequentTest(pure_datas)
    #OrderTest(pure_datas)
    OrderMergeTest(pure_datas, 'frequent', 'entry')


