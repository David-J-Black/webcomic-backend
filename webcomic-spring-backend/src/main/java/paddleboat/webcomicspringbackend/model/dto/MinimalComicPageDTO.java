package paddleboat.webcomicspringbackend.model.dto;

import lombok.Data;
import lombok.extern.slf4j.Slf4j;
import paddleboat.webcomicspringbackend.model.entitiy.ComicPage;

import java.time.Instant;

@Data
@Slf4j
public class MinimalComicPageDTO {
    private Integer pageNumber;
    private Integer chapterNumber;
    private Instant releaseDate;
    private String description;

    /**
     * Converts a ComicPage object to a MinimalComicPageDTO object.
     *
     * @param page the ComicPage object to be converted
     * @return the converted MinimalComicPageDTO object
     */
    public static MinimalComicPageDTO from(ComicPage page) {

        if (
                page.getChapter() == null
                || page.getChapter().getChapterNumber() == null
        ) {
            log.warn("Cannot create a MinimalComicPageDTO from an entity w/o" +
                    " a chapter number! [page: {}]", page);
            throw new RuntimeException("Problem processing page");
        }

        MinimalComicPageDTO response = new MinimalComicPageDTO();
        response.setPageNumber(page.getPageNumber());
        response.setReleaseDate(page.getReleaseDate());
        response.setDescription(page.getDescription());
        response.setChapterNumber(page.getChapter().getChapterNumber());
        return response;
    }
}
