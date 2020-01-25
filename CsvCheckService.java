
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.Objects;

/**
 * 公共检查服务
 * <p>
 * date: 2020-01-26
 * author: labu
 */
class CsvCheckService {
    public static final String SEPARATOR = ",";

    public static void main(String[] args) throws Exception {
        for (File file : Objects.requireNonNull(new File("data/").listFiles())) {
            if (file.getName().contains(".csv")) {
                checkCsv(file);
            }
        }

    }

    private static void checkCsv(File csvFile) throws Exception {
        BufferedReader reader = new BufferedReader(new FileReader(csvFile));
        String header = reader.readLine();
        int columns = header.split(SEPARATOR).length;
        int index = 1;
        String row;
        while ((row = reader.readLine()) != null) {
            int length = row.split(SEPARATOR).length;
            if (length != columns) {
                throw new RuntimeException(String.format("%s文件不符合CSV格式，例如：第%d行应该有%d行，而不是%d行", csvFile.getName(), index, columns, length));
            }
            index++;
        }
    }
}