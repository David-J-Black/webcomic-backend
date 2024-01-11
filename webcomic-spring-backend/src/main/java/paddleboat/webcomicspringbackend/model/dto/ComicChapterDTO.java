package paddleboat.webcomicspringbackend.model.dto;

import jakarta.annotation.Nullable;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.Instant;

@Data
@NoArgsConstructor
public class ComicChapterDTO {
    private Integer number;
    private String title;
    private Instant releaseDate;
    private String description;
    private Integer firstPage;
    private Integer lastPage;
    private Integer pageCount;

    @Nullable
    private ComicChapterDTO previousChapter;

    @Nullable
    private ComicChapterDTO nextChapter;
}
