package paddleboat.webcomicspringbackend.model.dto;

import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.extern.slf4j.Slf4j;
import paddleboat.webcomicspringbackend.model.entitiy.ComicPage;

@EqualsAndHashCode(callSuper = true)
@Data
@Slf4j
public class ComicPageDTO extends MinimalComicPageDTO {
    private ComicChapterDTO chapter;

    /**
     * Converts a ComicPage object to a ComicPageDTO object.
     * If the ComicPage object has no chapter, it throws a RuntimeException.
     *
     * @param page The ComicPage object to convert
     * @return The converted ComicPageDTO object
     * @throws RuntimeException if the ComicPage object has no chapter
     */
    public static ComicPageDTO from(ComicPage page) {

        if (page.getChapter() == null) {
            log.warn("Cannot make DTO from ComicPage object that has no chapter! [{}]", page);
            throw new RuntimeException("ComicPage conversion error: missing chapter!");
        }

        ComicPageDTO response = new ComicPageDTO();
        response.setPageNumber(page.getPageNumber());
        response.setReleaseDate(page.getReleaseDate());
        response.setDescription(page.getDescription());
        response.setChapterNumber(page.getChapter().getChapterNumber());
        ComicChapterDTO chapterDto = ComicChapterDTO
                .from(page.getChapter(), false, false);
        response.setChapter(chapterDto);

        return response;
    }
}
