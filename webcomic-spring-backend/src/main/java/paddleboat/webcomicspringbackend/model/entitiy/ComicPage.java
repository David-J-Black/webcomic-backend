package paddleboat.webcomicspringbackend.model.entitiy;

import jakarta.persistence.*;
import lombok.Data;

import java.time.Instant;

@Entity
@Data
@Table(name = "comic_page")
public class ComicPage {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long PageId;
    private Integer chapterId;
    private Integer pageNumber;
    private Instant releaseDate;
    private String description;
    private String pagePosition;
    private String imageName;
    private Instant createDt;
    private Instant updateDt;
    private String status;

    @Transient
    private ComicChapter chapter;
}