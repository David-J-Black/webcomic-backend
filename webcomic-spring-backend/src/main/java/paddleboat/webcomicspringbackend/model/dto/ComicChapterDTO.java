package paddleboat.webcomicspringbackend.model.dto;

import jakarta.annotation.Nullable;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.lang.NonNull;
import paddleboat.webcomicspringbackend.model.entitiy.ComicChapter;

import java.time.Instant;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

@Data
@Slf4j
@NoArgsConstructor
public class ComicChapterDTO {
    private Integer chapterNumber;
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

    @Nullable
    private List<MinimalComicPageDTO> pages;

    public static ComicChapterDTO from(@NonNull ComicChapter chapter,
                                       @Nullable Boolean includeNeighbors,
                                       @Nullable Boolean includePages) {

        ComicChapterDTO dto = new ComicChapterDTO();
        dto.setChapterNumber(chapter.getChapterNumber());
        dto.setTitle(chapter.getTitle());
        dto.setReleaseDate(chapter.getReleaseDate());
        dto.setDescription(chapter.getDescription());

        if ( chapter.getPages() != null ) {

            // If this chapter has pages, lets get the first and last page, and number of pages
            if (!chapter.getPages().isEmpty()) {
                Collection<Integer> pageNumbers = chapter.getPages().keySet();
                Integer firstPage = Collections.min(pageNumbers);
                Integer lastPage = Collections.max(pageNumbers);
                dto.setFirstPage(firstPage);
                dto.setLastPage(lastPage);
            }
            dto.setPageCount(chapter.getPages().size());

            // Attach pages if specified...
            if (includePages != null && includePages) {
                List<MinimalComicPageDTO> pages = new ArrayList<>();
                for (paddleboat.webcomicspringbackend.model.entitiy.ComicPage page : chapter.getPages().values()) {
                    pages.add(MinimalComicPageDTO.from(page));
                }
                dto.setPages(pages);
            }

        } else {
            log.warn("Noticed while making ComicChapterDTO" +
                    "that this chapter has no pages! [{}]", chapter);
            dto.setPageCount(0);
        }

        // Attach neighbors...
        if (includeNeighbors != null && includeNeighbors) {
            ComicChapter previousChapter = chapter.getPreviousChapter();
            if (previousChapter != null) {

                dto.setPreviousChapter(
                        ComicChapterDTO.from(previousChapter,
                        false,
                        false));
            }

            ComicChapter nextChapter = chapter.getNextChapter();
            if (nextChapter != null) {
                dto.setNextChapter(ComicChapterDTO.from(
                        nextChapter,
                        false,
                        false));
            }
        }

        return dto;
    }
}
