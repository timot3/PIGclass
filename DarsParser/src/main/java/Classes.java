import com.google.gson.annotations.SerializedName;

import java.util.ArrayList;

public class Classes {

    public class Required {
        String[][] courses;

        Required(String[][] courses){
            this.courses = courses;
        }
    }

    public class Finished {
        @SerializedName("courses") String[] names;
        Finished(String[] names){
            this.names = names;

        }
    }

    public class Electives {
        @SerializedName("courses") String[] names;
        Electives(String[] names){
            this.names = names;

        }
    }

    private ArrayList<String> names;
    Required requiredClasses;
    Finished finishedClasses;
    Classes(Required required, String[] finishedNames) {
        requiredClasses = required;
        finishedClasses = new Finished(finishedNames);
    }

}
