package paddleboat.webcomicspringbackend.service;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import paddleboat.webcomicspringbackend.model.PageIndex;
import paddleboat.webcomicspringbackend.model.dto.ComicPageDTO;
import paddleboat.webcomicspringbackend.service.cache.ComicCache;

import java.nio.file.Files;
import java.nio.file.Paths;

@Service
@RequiredArgsConstructor
@Slf4j
public class ComicPageService {

    private final ComicCache comicCache;

    public byte[] getComicPageImage(PageIndex pageIndex) throws Exception {
        try {
            log.info("Getting image for comic page [{}]", pageIndex);
            paddleboat.webcomicspringbackend.model.entitiy.ComicPage page = comicCache.getComicPage(pageIndex);

            if (page == null) {
                log.error("Null page! [{}]", pageIndex);
                throw new Error("Null Page!");
            }

            if (page.getImageName() == null) {
                log.error("Page has no image name! [page: {}]", page);
            }

            return Files.readAllBytes(Paths.get("./pages/" + page.getImageName()));
        } catch (Exception e) {
            log.info(System.getProperty("user.dir"));
            log.error("Error retreiving comic image", e);
            throw e;
        }
    }

    public ComicPageDTO getComicPage(PageIndex pageIndex) {
        paddleboat.webcomicspringbackend.model.entitiy.ComicPage comicPage = this.comicCache.getComicPage(pageIndex);

        if (comicPage == null) {
            log.warn("Got a null ComicPage from cache! [{}]", pageIndex);
            return null;
        }

        return ComicPageDTO.from(comicPage);
    }
}
