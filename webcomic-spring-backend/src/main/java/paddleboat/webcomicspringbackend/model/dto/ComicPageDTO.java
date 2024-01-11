package paddleboat.webcomicspringbackend.model.dto;

import lombok.Data;

import java.time.Instant;

@Data
public class ComicPageDTO {

    private Integer pageNumber;
    private Integer chapterNumber;
    private ComicChapterDTO chapter;
    private Instant releaseDate;
    private String description;
}
