package paddleboat.webcomicspringbackend.model.entitiy;

import jakarta.persistence.*;
import lombok.Data;

import java.time.LocalDate;
import java.util.HashMap;

@Entity
@Data
@Table(name = "comic_chapter")
public class ComicChapter {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long chapterId;
    private Integer chapterNumber;
    private String title;
    private LocalDate releaseDate;
    private String description;
    private LocalDate createdAt;
    private LocalDate updatedAt;
    private String status;

    @Transient
    private HashMap<Integer, ComicPage> pages;

}
