#### 1.创建空文件

```go
// 第一种：使用os.create
emptyFile, err := os.Create("empty.txt")
if err != nil {
    log.Fatal(err)
}
log.Println(emptyFile)
defer func() {
    err := emptyFile.Close()
    if err != nil {
        log.Println(err)
    }
}()
```

#### 2.创建空的文件夹

```go
// 获取文件的metadata的信息，如果不存在报：
// CreateFile test: The system cannot find the file specified.
_, err := os.Stat("test") 
fmt.Println(err) 
if os.IsNotExist(err) {
    // 创建文件夹
    errDir := os.MkdirAll("test", 0755)
    if errDir != nil {
        log.Fatal(err)
    }
}
```

#### 3.对文件或文件夹重命名

```go
oldName := "test.txt"
newName := "testing.txt"
err := os.Rename(oldName, newName)
if err != nil {
    log.Fatal(err)
}
```

#### 4.移动文件

`os.Rename()` 可以用来重命名和移动文件

```go
oldLocation := "/var/www/html/test.txt"
newLocation := "/var/www/html/src/test.txt"
err := os.Rename(oldLocation, newLocation)
if err != nil {
    log.Fatal(err)
}
```

#### 5.复制文件

`io.Coppy`是复制文件的关键

```go
package main
 
import (
	"io"
	"log"
	"os"
)
 
func main() {
 
	sourceFile, err := os.Open("/var/www/html/src/test.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer sourceFile.Close()
 
	// Create new file
	newFile, err := os.Create("/var/www/html/test.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer newFile.Close()
 
	bytesCopied, err := io.Copy(newFile, sourceFile)
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("Copied %d bytes.", bytesCopied)
}
```

#### 6.获取文件信息

```go
package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	fileStat, err := os.Stat("test.txt")

	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("文件名称:", fileStat.Name())       // Base name of the file
	fmt.Println("文件大小:", fileStat.Size())       // Length in bytes for regular files
	fmt.Println("权限:", fileStat.Mode())         // File mode bits
	fmt.Println("上一次修改时间:", fileStat.ModTime()) // Last modification time
	fmt.Println("是否是目录 ", fileStat.IsDir())         // Abbreviation for Mode().IsDir()
}
```

#### 7.删除文件

`os.Remove()`

```go
package main
 
import (
	"log"
	"os"
)
 
func main() {
	err := os.Remove("/var/www/html/test.txt")
	if err != nil {
		log.Fatal(err)
	}
}
```

#### 8.修改文件权限，时间戳

```go
package main
 
import (
	"log"
	"os"
	"time"
)
 
func main() {
	// Test File existence.
	_, err := os.Stat("test.txt")
	if err != nil {
		if os.IsNotExist(err) {
			log.Fatal("File does not exist.")
		}
	}
	log.Println("File exist.")
 
	// Change permissions Linux.
	err = os.Chmod("test.txt", 0777)
	if err != nil {
		log.Println(err)
	}
 
	// Change file ownership.
	err = os.Chown("test.txt", os.Getuid(), os.Getgid())
	if err != nil {
		log.Println(err)
	}
 
	// Change file timestamps.
	addOneDayFromNow := time.Now().Add(24 * time.Hour)
	lastAccessTime := addOneDayFromNow
	lastModifyTime := addOneDayFromNow
	err = os.Chtimes("test.txt", lastAccessTime, lastModifyTime)
	if err != nil {
		log.Println(err)
	}
}
```

#### 9.压缩文件到ZIP格式

```go
package main
 
import (
	"archive/zip"
	"fmt"
	"io"
	"log"
	"os"
)
 
func appendFiles(filename string, zipw *zip.Writer) error {
	file, err := os.Open(filename)
	if err != nil {
		return fmt.Errorf("Failed to open %s: %s", filename, err)
	}
	defer file.Close()
 
	wr, err := zipw.Create(filename)
	if err != nil {
		msg := "Failed to create entry for %s in zip file: %s"
		return fmt.Errorf(msg, filename, err)
	}
 
	if _, err := io.Copy(wr, file); err != nil {
		return fmt.Errorf("Failed to write %s to zip: %s", filename, err)
	}
 
	return nil
}
 
func main() {
	flags := os.O_WRONLY | os.O_CREATE | os.O_TRUNC
	file, err := os.OpenFile("test.zip", flags, 0644)
	if err != nil {
		log.Fatalf("Failed to open zip for writing: %s", err)
	}
	defer file.Close()
 
	var files = []string{"test1.txt", "test2.txt", "test3.txt"}
 
	zipw := zip.NewWriter(file)
	defer zipw.Close()
 
	for _, filename := range files {
		if err := appendFiles(filename, zipw); err != nil {
			log.Fatalf("Failed to add file %s to zip: %s", filename, err)
		}
	}
}
```

#### 10.读取ZIP文件中的文件

```go
package main
 
import (
	"archive/zip"
	"fmt"
	"log"
	"os"
)
 
func listFiles(file *zip.File) error {
	fileread, err := file.Open()
	if err != nil {
		msg := "Failed to open zip %s for reading: %s"
		return fmt.Errorf(msg, file.Name, err)
	}
	defer fileread.Close()
 
	fmt.Fprintf(os.Stdout, "%s:", file.Name)
 
	if err != nil {
		msg := "Failed to read zip %s for reading: %s"
		return fmt.Errorf(msg, file.Name, err)
	}
 
	fmt.Println()
 
	return nil
}
 
func main() {
	read, err := zip.OpenReader("test.zip")
	if err != nil {
		msg := "Failed to open: %s"
		log.Fatalf(msg, err)
	}
	defer read.Close()
 
	for _, file := range read.File {
		if err := listFiles(file); err != nil {
			log.Fatalf("Failed to read %s from zip: %s", file.Name, err)
		}
	}
}
```

#### 11.解压ZIP文件

```go
package main
 
import (
	"archive/zip"
	"io"
	"log"
	"os"
	"path/filepath"
)
 
func main() {
	zipReader, _ := zip.OpenReader("test.zip")
	for _, file := range zipReader.Reader.File {
		zippedFile, err := file.Open()
		if err != nil {
			log.Fatal(err)
		}
		defer zippedFile.Close()
 
		targetDir := "./"
		extractedFilePath := filepath.Join(
			targetDir,
			file.Name,
		)
 
		if file.FileInfo().IsDir() {
			log.Println("Directory Created:", extractedFilePath)
			os.MkdirAll(extractedFilePath, file.Mode())
		} else {
			log.Println("File extracted:", file.Name)
 
			outputFile, err := os.OpenFile(
				extractedFilePath,
				os.O_WRONLY|os.O_CREATE|os.O_TRUNC,
				file.Mode(),
			)
			if err != nil {
				log.Fatal(err)
			}
			defer outputFile.Close()
 
			_, err = io.Copy(outputFile, zippedFile)
			if err != nil {
				log.Fatal(err)
			}
		}
	}
}
```











