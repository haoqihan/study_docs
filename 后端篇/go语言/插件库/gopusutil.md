### gopsutil

psutil是一个跨平台进程和系统监控的Python库，而gopsutil是其Go语言版本的实现。本文介绍了它的基本使用。

Go语言部署简单、性能好的特点非常适合做一些诸如采集系统信息和监控的服务，本文介绍的gopsutil库是知名Python库：psutil的一个Go语言版本的实现。

###  安装

```
    go get github.com/shirou/gopsutil
```

### 使用

#### CPU

采集CPU相关信息。

```go
import "github.com/shirou/gopsutil/cpu"

// cpu info
func getCpuInfo() {
    cpuInfos, err := cpu.Info()
    if err != nil {
        fmt.Printf("get cpu info failed, err:%v", err)
    }
    for _, ci := range cpuInfos {
        fmt.Println(ci)
    }
    // CPU使用率
    for {
        percent, _ := cpu.Percent(time.Second, false)
        fmt.Printf("cpu percent:%v\n", percent)
    }
}
```

获取CPU负载信息：

```go
import "github.com/shirou/gopsutil/load"

func getCpuLoad() {
    info, _ := load.Avg()
    fmt.Printf("%v\n", info)
}
```

#### Memory

```go
import "github.com/shirou/gopsutil/mem"

// mem info
func getMemInfo() {
    memInfo, _ := mem.VirtualMemory()
    fmt.Printf("mem info:%v\n", memInfo)
}
```

#### Host

```go
import "github.com/shirou/gopsutil/host"

// host info
func getHostInfo() {
    hInfo, _ := host.Info()
    fmt.Printf("host info:%v uptime:%v boottime:%v\n", hInfo, hInfo.Uptime, hInfo.BootTime)
}
```

#### Disk

```go
import "github.com/shirou/gopsutil/disk"

// disk info
func getDiskInfo() {
    parts, err := disk.Partitions(true)
    if err != nil {
        fmt.Printf("get Partitions failed, err:%v\n", err)
        return
    }
    for _, part := range parts {
        fmt.Printf("part:%v\n", part.String())
        diskInfo, _ := disk.Usage(part.Mountpoint)
        fmt.Printf("disk info:used:%v free:%v\n", diskInfo.UsedPercent, diskInfo.Free)
    }

    ioStat, _ := disk.IOCounters()
    for k, v := range ioStat {
        fmt.Printf("%v:%v\n", k, v)
    }
}
```

#### net IO

```go
import "github.com/shirou/gopsutil/net"

func getNetInfo() {
    info, _ := net.IOCounters(true)
    for index, v := range info {
        fmt.Printf("%v:%v send:%v recv:%v\n", index, v, v.BytesSent, v.BytesRecv)
    }
}
```

#### 获取本机IP的两种方式

```go
func GetLocalIP() (ip string, err error) {
    addrs, err := net.InterfaceAddrs()
    if err != nil {
        return
    }
    for _, addr := range addrs {
        ipAddr, ok := addr.(*net.IPNet)
        if !ok {
            continue
        }
        if ipAddr.IP.IsLoopback() {
            continue
        }
        if !ipAddr.IP.IsGlobalUnicast() {
            continue
        }
        return ipAddr.IP.String(), nil
    }
    return
}
```

或：

```go
// Get preferred outbound ip of this machine
func GetOutboundIP() string {
    conn, err := net.Dial("udp", "8.8.8.8:80")
    if err != nil {
        log.Fatal(err)
    }
    defer conn.Close()

    localAddr := conn.LocalAddr().(*net.UDPAddr)
    fmt.Println(localAddr.String())
    return localAddr.IP.String()
}
```


