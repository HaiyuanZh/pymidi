## 使用 MIDIUtil库
- 安装

    pip install MIDIUtil

- 生成文件
```
with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
```

- 解读

    通过循环
```
for i, pitch in enumerate(degrees):
    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)
```
    增加midi内容，要想研究透，就需要把midi文件格式原理搞清楚，才能理解用midi做电音


## 使用 mido
- 安装

这里需要注意的是，mido需要backend的支持，单独安装mido没用
```
pip install mido
pip install python-rtmidi
```
其中 python-rtmidi 是mido库默认的推荐backend，有了backend，mido库才能起作用

代码都是官方的，都能用