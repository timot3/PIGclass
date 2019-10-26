import com.google.gson.annotations.SerializedName;

import java.util.ArrayList;

public class Finished {
    @SerializedName("courses") String[] names;
    Finished(String[] names){
        this.names = names;

    }
}
