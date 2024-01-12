package paddleboat.webcomicspringbackend.model.entitiy;

import jakarta.persistence.*;
import lombok.Data;
import lombok.ToString;

import java.time.Instant;
import java.util.LinkedHashMap;

@Entity
@Data
@ToString(exclude = {"previousChapter", "nextChapter", "pages"})
@Table(name = "comic_chapter")
public class ComicChapter {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long chapterId;
    private Integer chapterNumber;
    private String title;
    private Instant releaseDate;
    private String description;
    private Instant createdAt;
    private Instant updatedAt;
    private String status;

    @Transient
    private LinkedHashMap<Integer, ComicPage> pages;

    @Transient
    private ComicChapter previousChapter;

    @Transient
    private ComicChapter nextChapter;

}
